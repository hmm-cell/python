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
    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {len(valid_scores)}")
    print(f"Total score: {sum(valid_score)}")
    print(f"Average score: {(valid_score)}")
