from flask import render_template

def not_found(url):
    return render_template('errors/404.html', url=url), 404

def not_authorised(url):
    return render_template('errors/401.html', url=url), 401

def forbidden(url):
    return render_template('errors/403.html', url=url), 403

def server_error(url):
    return render_template('errors/500.html', url=url), 500
