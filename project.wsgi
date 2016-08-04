#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/kpacitor/")

activate_this = '/var/www/kpacitor/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from project import app as application
application.secret_key = 'Add your secret key'
Contact GitHub API Training Shop Blog About
