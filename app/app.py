from flask import Flask, render_template, request
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
        return functions.handle_request('proxypage', route_details)
    else:
        return errors.not_found(path)


### Search handler, talks to search service ###
@app.route('/search')
def search():
    key, route_details = t.longest_prefix('/search')
    try:
        route_details['params']['search_string'] = request.args.get('search')
    except:
        route_details['params']['search_string'] = None
    if route_details['params']['search_string']:
        return functions.handle_request('searchpage', route_details)
    else:
        return render_template('searchpage.html', route_details=route_details), 200


### Authentication handlers ###
@app.route('/authentication/login')
def login():
    return "login handler"
