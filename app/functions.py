from flask import render_template
import requests
import json


def read_route_file(filepath, local):
    f = open(filepath, 'r')
    routes = json.loads(f.read())
    return routes


def load_trie(filepath, t, local=True):
    routes = read_route_file(filepath, local)
    for route in routes:
        if route != 'home':
            t[routes[route]['route']] = routes[route]
            print(route)
    print("LOADED")
    return t


def load_root(filepath, local=True):
    routes = read_route_file(filepath, local)
    return routes['home']


def handle_request(template_name, route_details):
    try:
        data = fetch_url('https://drchristhorpe.github.io/')
    except:
        data = None

    return render_template(template_name + '.html', route_details=route_details, data=data), 200


def fetch_url(url, format='html'):
    r = requests.get(url)
    return r.text
