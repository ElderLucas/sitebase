#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
import httplib2
import os
from flask import make_response
import requests
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


app = Flask(__name__)


APPLICATION_NAME = "Restaurant Menu Application"

# Show all restaurants
@app.route('/')
def redirect_kpacitor():
    return redirect("http://http://kpacitor.teachable.com/courses/raspberry")

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    #app.debug = True
    app.run(host='0.0.0.0', port=5000)