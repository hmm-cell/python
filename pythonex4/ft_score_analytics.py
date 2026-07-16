import sys

print(f"=== Player Score Analytics ===")

valid_scores = []
invalid_scores = []

for arg in sys.argv[1: ]:
    try:
        num = int(arg)
        valid_scores.append(num)
    except ValueError:
        invalid_scores.append(arg)

if len(invali_params) > 0:
    for param in invalid_scores:
        print(f"Invalid parameter: '{param}'")

if len(valid_scores) == 0:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    total_score = sum(valid_scores)
    avg_score = total_score / len(valid_scores)
    score_range = max(valid_scores) - min(valid_scores)
    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {len(valid_scores)}")
    print(f"Total score: {sum(valid_scorea)}")
    print(f"Average score: {avg_score}")
    print(f"High score: {max(valid_scores)}")
    print(f"Low score: {min(valid_scorea)}")
    print(f"Score range: {score_range}")
