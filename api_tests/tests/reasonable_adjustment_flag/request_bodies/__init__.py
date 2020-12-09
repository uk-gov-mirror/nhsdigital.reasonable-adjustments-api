import json
import sys
import os

pwd = os.path.dirname(__file__)

with open(pwd + '/POST_Consent.json') as json_file:
    POST_Consent = json.load(json_file)

with open(pwd + '/PUT_Consent.json') as json_file:
    PUT_Consent = json.load(json_file)

with open(pwd + '/POST_removerarecord.json') as json_file:
    POST_removerarecord = json.load(json_file)

with open(pwd + '/POST_Flag.json') as json_file:
    POST_Flag = json.load(json_file)

with open(pwd + '/PUT_Flag.json') as json_file:
    PUT_Flag = json.load(json_file)

with open(pwd + '/POST_List.json') as json_file:
    POST_List = json.load(json_file)

