from flask import render_template, Markup
import requests
import json
import markdown

import logging

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
    url = route_details['root']
    if 'url' in route_details and route_details['strip']:
        try:
            url = url + route_details['url'].replace(route_details['strip'],'')
        except:
            url = url
    if 'format' in route_details and route_details['format'] == 'json':
        status, data = fetch_url(route_details['root'])
        data = json.loads(data)
    elif 'format' in route_details and route_details['format'] == 'markdown':
        status, data = fetch_url(route_details['root'])
        data = Markup(markdown.markdown(data))
    else:
        status, data = fetch_url(url)

    if data:
        return render_template(template_name + '.html', route_details=route_details, data=data), 200
    else:
        return render_template('errors/' + str(status) + '.html', route_details=route_details), status


def fetch_url(url, format='html'):
    r = requests.get(url)
    if r.status_code == 200:
        return 200, r.text
    else:
        return r.status_code, False
