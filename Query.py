import urllib.request
import json
import csv
import pandas as pd

# New function that saves data to a CSV
def player_info(memberTag):
    # Keeps authentication key open for each transaction
    token = 'clashkey.txt'
    request = urllib.request.Request(
        url,
        None,
        {
            "Authorization": "Bearer %s" % token
        }
    )
    member_response = urllib.request.urlopen(request).read().decode("utf-8")
    member_data = json.loads(member_response)
    return member_data

def battle_log(memberTag):
    token = 'clashkey.txt'
    url = "https://api.clashroyale.com/v1/players/%23" + str(memberTag) + '/battlelog'

    request = urllib.request.Request(
        url,
        None,
        {
            "Authorization": "Bearer %s" % token
        }
    )
    member_response = urllib.request.urlopen(request).read().decode("utf-8")
    member_data = json.loads(member_response)
    return member_data


print(battle_log('YYRVLLUV'))
