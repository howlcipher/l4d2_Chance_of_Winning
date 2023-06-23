import yaml

def calculate_win_chance(team1_score, team2_score, points_remaining):
    max_possible_score = team1_score + team2_score + points_remaining
    team1_chance = (team1_score / max_possible_score) * 100
    team2_chance = (team2_score / max_possible_score) * 100

    # Adjust win chances based on remaining points
    if team1_score + points_remaining <= team2_score:
        team1_chance = 0
        team2_chance = 100
    elif team2_score + points_remaining <= team1_score:
        team1_chance = 100
        team2_chance = 0

    return team1_chance, team2_chance

# Read input from YAML file
file_name = "config.yaml"
with open(file_name, "r") as file:
    game_data = yaml.safe_load(file)

team1_score = game_data["team1"]
team2_score = game_data["team2"]
points_remaining = game_data["points_remaining"]

# Calculate win chances
team1_chance, team2_chance = calculate_win_chance(team1_score, team2_score, points_remaining)

# Print the results
print("Team One has a {:.2f}% chance of winning.".format(team1_chance))
print("Team Two has a {:.2f}% chance of winning.".format(team2_chance))
