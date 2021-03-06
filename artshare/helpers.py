from functools import wraps
from flask import session, redirect, url_for, flash

# Decorator helper functions to be used for routes


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Please login to view page', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def loggedout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' in session:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
