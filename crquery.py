# A lambda function to interact with AWS RDS MySQL

import pymysql
import sys
import requests

rds_host = #removed
name = #removed
password = #removed
db_name = #removed


def call_clash():
    url = "https://api.clashroyale.com/v1/players/%23" + 'YYRVLLUV'

    headers = {"Accept": "application/json",
               "authorization": "Bearer #removed key
               }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    tag = data['tag']
    username = data['name']
    expLevel = data['expLevel']
    trophies = data['trophies']
    wins = data['wins']
    losses = data['losses']
    bestTrophies = data['bestTrophies']
    print('data is loaded')
    return tag, username, expLevel, trophies, wins, losses, bestTrophies


def save_events():
    """
    This function inserts data into the MYSQL RDS instance
    """
    print('save events function start')
    tag, username, level, trophies, wins, losses, besttrophies = call_clash()
    print('line before connection made')
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, connect_timeout=10)
    print('connection made')
    with conn.cursor() as cur:
        cur.execute("""insert into player_info.player (tag, username, level, trophies, wins, losses, besttrophies)
                    values( '%s', '%s', %s, %s, %s, %s, %s)""" % #('test','testname', 2, 3, 4, 5, 6))
                    (tag, username, level, trophies, wins, losses, besttrophies))
        conn.commit()
        cur.close()
    return 'success'


def main(event, context):
    print('start')
    save_events()
