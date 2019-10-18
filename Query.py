import urllib.request
import json
import csv
import pandas as pd

# New function that saves data to a CSV
def player_info(memberTag):
    # Keeps authentication key open for each transaction
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE5OTQxN2RmLTFiYmItNDA2NS05NGJiLWIzMDliYzQ4MGUzYSIsImlhdCI6MTU3MDUxMTcxMywic3ViIjoiZGV2ZWxvcGVyLzVkYmE4NzhjLWZiOWUtYTVlYy1lNGUyLWVkN2U3NjQ5NDcyOCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0Ny4xOTcuMjQuMTU1Il0sInR5cGUiOiJjbGllbnQifV19.Nr_ek-ihH3bDRK384OTGLu5qGeazQePUa9_nZUz1M-dHnWsICXbSSxuh0loms30AHI9p7EgxGL51vIKT8h8VdQ'
    url = "https://api.clashroyale.com/v1/players/%23" + str(memberTag)

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
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE5OTQxN2RmLTFiYmItNDA2NS05NGJiLWIzMDliYzQ4MGUzYSIsImlhdCI6MTU3MDUxMTcxMywic3ViIjoiZGV2ZWxvcGVyLzVkYmE4NzhjLWZiOWUtYTVlYy1lNGUyLWVkN2U3NjQ5NDcyOCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0Ny4xOTcuMjQuMTU1Il0sInR5cGUiOiJjbGllbnQifV19.Nr_ek-ihH3bDRK384OTGLu5qGeazQePUa9_nZUz1M-dHnWsICXbSSxuh0loms30AHI9p7EgxGL51vIKT8h8VdQ'
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