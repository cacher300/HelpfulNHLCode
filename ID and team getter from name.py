import requests
import json

base1 = ['Evgeni Malkin', 'Sidney Crosby', 'Quinn Hughes']
base2 = ['Connor McDavid', 'Leon Draisaitl', 'Mitch Marner']
base3 = ['Jack Eichel', 'Jack Hughes', 'Matthew Tkachuk']

# Set the base URL for the NHL API
base_url = "https://statsapi.web.nhl.com/api/v1"

# Send a GET request to the teams endpoint and load the response into a JSON object
response = requests.get(f"{base_url}/teams")
teams = json.loads(response.text)

part1 = []
part2 = []
part3 = []

# Iterate through each team in the response
for team in teams["teams"]:
    # Get the team ID and name
    team_id = team["id"]
    team_name = team["name"]

    # Set the endpoint for retrieving the roster for this team
    roster_endpoint = f"/teams/{team_id}/roster"

    # Send a GET request to the roster endpoint and load the response into a JSON object
    response = requests.get(base_url + roster_endpoint)
    roster = json.loads(response.text)

    # Iterate through each player on this team's roster
    for player in roster["roster"]:
        # Get the player ID and name
        player_id = player["person"]["id"]
        player_name = player["person"]["fullName"]

        # Check if the player's name is in base1
        if player_name in base1:
            # Append the player's team ID and player ID to part1
            part1.append({"name": player_name, "team_id": team_id, "player_id": player_id})
        # Check if the player's name is in base2
        elif player_name in base2:
            # Append the player's team ID and player ID to part2
            part2.append({"name": player_name, "team_id": team_id, "player_id": player_id})
        # Check if the player's name is in base3
        elif player_name in base3:
            # Append the player's team ID and player ID to part3
            part3.append({"name": player_name, "team_id": team_id, "player_id": player_id})
print(part1)
print(part2)
print(part3)
