import pandas as pd
import json, random, os

def _generate_json_doc():
    '''
    Goes through all quotes and generates a JSON Document with the following pattern:

    # "a b c a b k"
    # {'a b': ['c','k'], 'b c': ['a'], 'c a': ['b']}
    # Algorithm Inspired From:
    # http://stackoverflow.com/questions/5306729/how-do-markov-chain-chatbots-work/5307230#5307230
    '''

    data = pd.read_csv("data.csv")
    # Get all the quotes
    quotes = [quote for quote in data["text"]]

    # Set up a dictionary to store the quotes in a tree like structure
    markov_dict = {}

    # for each quote, set up all possible combinations
    for quote in quotes:
        for w1, w2, w3 in _triple_sets(quote):
            # Do not allow the words to contain  "\"" and do not copy expressions that are urls.
            if _check_url(w1, w2, w3):
                markov_dict.setdefault(' '.join((w1, w2)), []).append(w3)

    # Prettyprint a sorted list of the markov dict into a text file
    json_text = json.dumps(markov_dict, indent=4, sort_keys=True)
    with open("data_out.json", "w") as f:
        f.write(json_text)

def _triple_sets(sentence):
    '''
    Helper method which will generate all possible combinations of (w1,w2,w3)
    in a single string.
    '''
    sentence_list = sentence.split()
    for i in range(len(sentence_list) - 2):
        yield (sentence_list[i], sentence_list[i + 1], sentence_list[i + 2])

def _check_url(w1, w2, w3):
    '''
    Method to check if a 3 tuple set contains a url.
    '''
    return not (re.match("http.*", w1) or re.match("http.*", w2) or re.match("http.*", w3))

def _load_json_doc():
    # Loading the json document into the object field.
    with open("data_out.json") as json_doc:
        json_tree = json.load(json_doc)
    return json_tree

def generate_random_tweet(length=1, proper_caps=False, tweets_loaded=False):
    '''
    Using the document generated in the initialization step, generate a tweet
    by executing a random walk on the markov chain.
    '''
    if not tweets_loaded or os:
        _generate_json_doc()

    json_tree = _load_json_doc()

    # Start with Empty String
    tweet = ""
    key = random.choice(list(json_tree.keys()))
    tweet += key.split(' ')[0] + ' '
    sentences = 0
    while sentences < length:
        tweet += key.split(' ')[1] + ' '
        try:
            value = random.choice(json_tree[key])
        except KeyError as e:
            key = random.choice(list(json_tree.keys()))
        else:
            word1, word2 = key.split(" ")
            key = ' '.join([word2, value])

        if  tweet[-2] in ".?!":
            sentences += 1

    if proper_caps:
        return _proper_capitalization(tweet)
    else:
        return tweet


def _proper_capitalization(sentence):
    '''
    Ensure that the generated tweet has proper capitalization.
    '''
    sentence_list = sentence.split()

    # always capitalize the first letter
    if sentence_list[0][0].isalpha():
        sentence_list[0] = sentence_list[0][0].upper() + sentence_list[0][1:]

    for i, c in enumerate(sentence_list):
        if c[-1] in ".?!" and i != len(sentence_list)-1:
            sentence_list[i+1] = sentence_list[i+1][0].upper() + sentence_list[i+1][1:]

    return ' '.join(sentence_list)
