import requests
import json
import logging
import os
import re
import string
from pprint import pprint
import collections.abc
import array
import collections.abc

accesstoken = ''
botid = ''
groupid = ''
payload = {"bot_id":botid, "text":"Hello, you executed the program!"}
getfunction = '/groups/' + groupid + '/messages'
postfunction = '/bots/post'
url = 'https://api.groupme.com/v3'
messagestosearch = 20 #How many messages to search
findword = 'Test' #The requested word to find


g = requests.get(url + getfunction + '?token=' + accesstoken, messagestosearch)
lod = json.loads(g.text)

x = 0
itercount = 0
while x <= messagestosearch:
    if (lod['response']['messages'][x]['sender_type']) != 'bot':
        if findword.lower() in (lod['response']['messages'][x]['text']).lower():
            itercount = itercount + 1

    x += 1
    if x == messagestosearch:
        break

requests.post(url + postfunction, {"bot_id":botid, "text":"I see " + str(itercount) + " case-insensitive instances of the word you requested, " + '\"' + findword + '\".'}) #Posts the response to chat
