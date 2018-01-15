from flask import Blueprint, session, request, render_template, redirect, url_for,redirect, make_response
from passlib.hash import sha256_crypt
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, RadioField, widgets, SelectMultipleField

from functools import wraps
import time

from datetime import datetime,timedelta 

portal = Blueprint('ws_portal', __name__)

# flask web html  
# The 'templates' file must stroage .hmtl
@portal.route('/')
def home():
    return render_template('home.j2.html', name = '成功')

# function redirect to home() 
@portal.route('/login')
def login():

    return redirect(url_for('/'))
