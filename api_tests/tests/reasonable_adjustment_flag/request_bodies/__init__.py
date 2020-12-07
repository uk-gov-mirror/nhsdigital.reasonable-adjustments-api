import json
import sys
import os

pwd = os.path.dirname(__file__)

with open(pwd + '/POST_Consent.json') as json_file:
    POST_Consent = json.load(json_file)

