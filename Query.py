import requests
import json

# New function that saves data to a CSV
def player_info(memberTag):
    url = "https://api.clashroyale.com/v1/players/%23" + str(memberTag)

    headers = {"Accept": "application/json",
               "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZlNzUyMmMyLTZiZjMtNGUyYS04YmUwLWM0YzdkMWQ1MjM0ZiIsImlhdCI6MTU3NDIxNjI5MCwic3ViIjoiZGV2ZWxvcGVyLzVkYmE4NzhjLWZiOWUtYTVlYy1lNGUyLWVkN2U3NjQ5NDcyOCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC44OC4yNDIuMTE3Il0sInR5cGUiOiJjbGllbnQifV19.2jMHppUrsLN9o2AfIyk1JBe96iIrcI2YhKUHrWI3RsrD_H4npoXPyHypTjZEXuPIGTaeaIGT6lcTewjUJkXwBA"
               }

    response = requests.request("GET", url, headers=headers)
    #print(response.text)
    data = response.json()
    tag = data['tag']
    username = data['name']
    expLevel =  data['expLevel']
    trophies = data['trophies']
    wins = data['wins']
    losses = data['losses']
    bestTrophies = data['bestTrophies']
    
    return tag, username, expLevel, trophies, wins, losses, bestTrophies


tag, user, expLevel,trophies, wins,losses, best = player_info('YYRVLLUV')


