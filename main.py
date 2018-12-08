# Serverless Application

from flask import escape
from gen import generate_random_tweet
from random import randrange

def tweet_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': ['GET','POST'],
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    # Change to website when complete
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'length' in request_json:
        length = request_json['length']
    elif request_args and 'name' in request_args:
        length = request_args['length']
    else:
        length = randrange(1,3)

    return (generate_random_tweet(length, proper_caps=True, tweets_loaded=True), 200, headers)
