# Serverless Application

from flask import escape
from gen import generate_random_tweet
from random import randrange

def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json(silent=True)

    if request_json and 'length' in request_json:
        return generate_random_tweet(length=request_json['length'], proper_caps=True)

    return generate_random_tweet(length=randrange(1,3), proper_caps=True)
