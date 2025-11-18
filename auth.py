from functools import wraps
from flask import session, redirect, url_for

USERS = {
    "student1": "password1",
    "professor1": "password2",
}

def authenticate(username, password):
    return username in USERS and USERS[username] == password

def login_required(f):
    @wraps(f) 
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args,**kwargs)
    return wrapper
