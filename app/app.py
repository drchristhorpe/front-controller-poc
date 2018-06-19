from flask import Flask
import pygtrie
import logging
import json
import errors
import functions


filepath = 'routes.json'

app = Flask(__name__)
t = functions.load_trie(filepath, pygtrie.CharTrie())


### Handlers ###

### Catch all handler ###
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    path = '/' + path
    key, handler = t.longest_prefix(path)
    if key is not None:
        handler['url'] = path
        text = json.dumps(handler)
        return text
    else:
        return errors.not_found(path)


### Reload handler, for hot reloading of the routing and paywall Trie ###
@app.route('/reload')
def reload():
    t = functions.load_trie(filepath, pygtrie.CharTrie())
    return 'reloaded'


### Search handler, talks to search service ###
@app.route('/search')
def search():
    return "search handler"


### Authentication handlers ###
@app.route('/authentication/login')
def login():
    return "login handler"
