import urllib.request
import json
import csv

# Creates a list containing the clan tag of each member of a given clan, then writes each members profile information to a CSV file.
# inputted clan tag must not contain a hashtag
def clan_member_list_generator(clanTag):
    with open("clashkey.txt") as f:
        my_key = f.read().rstrip("\n")
        base_url = "https://api.clashroyale.com/v1"
        endpoint = "/clans/%23" + str(clanTag) + "/members"

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

#When given a member's tag, will return all information about that player.
def individual_member_info_generator(memberTag):
    with open("clashkey.txt") as f:
        with open('member.csv', 'w', newline='') as i:
            my_key = f.read().rstrip("\n")
            base_url = "https://api.clashroyale.com/v1"
            thewriter = csv.writer(i)
            thewriter.writerow(['Name', 'Tag', 'Trophies', 'Wins', 'Losses', 'Challenge Cards Won', 'Challenge Max Wins',
                                'Donations', 'Donations Received', 'War Day Wins', 'Clan Cards Collected'])

            # CSV File Entry, Get information about each member then add to CSV
            # the member JSON has more info than the clan details, so I need another request

            member_endpoint = "/players/%23" + str(memberTag)
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

individual_member_info_generator("YYRVLLUV")
