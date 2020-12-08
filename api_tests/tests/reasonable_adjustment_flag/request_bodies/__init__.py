import json
import sys
import os

pwd = os.path.dirname(__file__)

with open(pwd + '/POST_Consent.json') as json_file:
    POST_Consent = json.load(json_file)

with open(pwd + '/PUT_Consent.json') as json_file:
    PUT_Consent = json.load(json_file)

with open(pwd + '/POST_raremoverecord.json') as json_file:
    POST_raremoverecord = json.load(json_file)

with open(pwd + '/POST_Flag.json') as json_file:
    POST_Flag = json.load(json_file)

