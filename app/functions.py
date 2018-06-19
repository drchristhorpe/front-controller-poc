from flask import render_template
import json


def load_trie(filepath, t, local=True):
    f = open(filepath, 'r')
    routes = json.loads(f.read())
    for route in routes:
        t[routes[route]['route']] = routes[route]
        print(route)
    print("LOADED")
    return t


def handle_request(handler):
    return render_template('proxypage.html', handler=handler), 200
