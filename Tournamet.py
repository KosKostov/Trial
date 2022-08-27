number_of_teams = input("Enter the number of teams in the tournament: ")
while number_of_teams.isdigit() == False:
    print("Enter a valid number of teams: ")
    number_of_teams = input("Enter the number of teams in the tournament: ")
while int(number_of_teams) < 2:
    print("The minimum number of teams is 2, try again")
    number_of_teams = int(input("Enter the number of teams in the tournament: "))
teams = [None for _ in range(int(number_of_teams))]
for i in range(int(number_of_teams)):
    team = input(f"Enter the name of team #{i+1}")
    while len(team) < 2:
        print("Team names must have at least 2 characters, try again.")
        team = input(f"Enter the name of team #{i+1}")
    while len(team.split()) > 2:
        print("Team names may have at most 2 words, try again.")
        team = input(f"Enter the name of team #{i+1}")
    teams[i] = team

number_of_games = input("Enter the number of games played by each team")

while number_of_games.isdigit() == False or int(number_of_games) < int(number_of_teams):
    print("Invalid number of games. Each team plays each other at least once in the regular season.")
    number_of_games = input("Enter the number of games played by each team")

results = {team: None for team in teams}
for i, team in enumerate(teams):
    wins = input(f"Enter the number of wins team {team} had: ")
    while int(wins) < 0:
        print("The minimum number of wins is 0, try again.")
        wins = input(f"Enter the number of wins team {team} had: ")
    while int(wins) > int(number_of_games):
        print(f"The maximum number of wins is {number_of_games}, try again.")
        wins = input(f"Enter the number of wins team {team} had: ")
    results[team] = int(wins)
print(results)

score = list(results.values())
print("Generating the games to be played in the first round of the tournament...")
while score != []:
    maximum = score.pop(score.index(max(score)))
    minimum = score.pop(score.index(min(score)))
    print(f"Home: {minimum} VS AWAY: {maximum}")