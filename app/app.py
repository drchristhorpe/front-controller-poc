from flask import Flask
import pygtrie
import logging
import json
import errors
import functions


filepath = 'routes.json'

app = Flask(__name__)
t = functions.load_trie(filepath, pygtrie.CharTrie())
root = functions.load_root(filepath)

### Handlers ###

### Catch all handler ###
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    path = '/' + path
    route_details = None

    if path == '/':
        route_details = root
        route_details['url'] = path
    else:
        key, route_details = t.longest_prefix(path)
        if key is not None:
            route_details['url'] = path
            
    if route_details is not None:
        return functions.handle_request(route_details)
    else:
        return errors.not_found(path)


### Reload handler, for hot reloading of the routing and paywall Trie ###
@app.route('/reload')
def reload():
    t = functions.load_trie(filepath, pygtrie.CharTrie())
    root = functions.load_root(filepath)
    return 'reloaded'


### Search handler, talks to search service ###
@app.route('/search')
def search():
    return "search handler"


### Authentication handlers ###
@app.route('/authentication/login')
def login():
    return "login handler"
