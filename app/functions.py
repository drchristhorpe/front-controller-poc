import json


def load_trie(filepath, t, local=True):
    f = open(filepath, 'r')
    routes = json.loads(f.read())
    for route in routes:
        t[routes[route]['route']] = routes[route]
        print(route)
    print("LOADED")
    return t
