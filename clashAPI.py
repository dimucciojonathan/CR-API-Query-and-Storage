import urllib.request
import json
import csv

# Every API request requires IP authorization
with open("clashkey.txt") as f:
    my_key = f.read().rstrip("\n")
    base_url = "https://api.clashroyale.com/v1"
    endpoint = "/clans/%239YRULYJY/members"

    # first request gives us details about each member in the clan (I want to extract member ID's)
    request = urllib.request.Request(
        base_url + endpoint,
        None,
        {
            "Authorization": "Bearer %s" % my_key
        }
    )

    response = urllib.request.urlopen(request).read().decode("utf-8")
    data = json.loads(response)

    # data gives us all given information about each clan member
    tag_list = []
    for item in data["items"]:
        tag_item = item["tag"]
        tag_item = tag_item[1:len(item["tag"])]
        tag_list.append(tag_item)

    outputFile = open("ConvertedJSON.csv", "w")
    outputWriter = csv.writer(outputFile)

    # Now I want to loop through the player list and get info about each player while writing it to a csv
    with open('persons.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Name', 'Tag', 'Trophies', 'Wins', 'Losses', 'Challenge Cards Won', 'Challenge Max Wins',
                            'Donations', 'Donations Received', 'War Day Wins', 'Clan Cards Collected'])

        # CSV File Entry, Get information about each member then add to CSV
        # the member JSON has more info than the clan details, so I need another request
        for i in range(len(tag_list)):
            member_endpoint = "/players/%23" + tag_list[i]
            request2 = urllib.request.Request(
                base_url + member_endpoint,
                None,
                {
                    "Authorization": "Bearer %s" % my_key
                }
            )
            member_response = urllib.request.urlopen(request2).read().decode("utf-8")
            member_data = json.loads(member_response)
            # I got an error for one member, so I used try/except to keep the code going.
            try:
                thewriter.writerow([member_data["name"], member_data["tag"], member_data["trophies"],
                                    member_data["wins"], member_data["losses"], member_data["challengeCardsWon"],
                                    member_data["challengeMaxWins"], member_data["donations"],
                                    member_data["donationsReceived"], member_data["warDayWins"],
                                    member_data["clanCardsCollected"],
                                    ])
            except:
                pass