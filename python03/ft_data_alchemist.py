import random

names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
print(f"Initial list of players: {names}")

capitalize_names = [name.capitalize() for name in names]
print(f"New list with all names capitalized: {capitalize_names}")

capitalized_names = [name for name in names if name[0].isupper()]
print(f"New list of capitalized names only: {capitalized_names}")

player_scores = {name: random.randint(1, 1000) for name in capitalize_names}
print(f"Score list: {player_scores}")

avg_score = (sum(player_scores.values()) / len(player_scores.keys()))
print(f"Score average is {avg_score}")

scores_remaining = [[name, score] for name, score in player_scores.items()]
high_scores_ordered = {}

for _ in range(len(scores_remaining)):
    highest_pair = scores_remaining[0]
    for pair in scores_remaining:
        if pair[1] > highest_pair[1]:
            highest_pair = pair
    high_scores_ordered[highest_pair[0]] = highest_pair[1]
    scores_remaining.remove(highest_pair)

print(f"High scores: {high_scores_ordered}")
