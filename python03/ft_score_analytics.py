import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    valid_scores: list[int] = []
    invalid_scores: list[str] = []

    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            valid_scores.append(num)
        except ValueError:
            invalid_scores.append(arg)

    if len(invalid_scores) > 0:
        for param in invalid_scores:
            print(f"Invalid parameter: '{param}'")

    if len(valid_scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2>"
        )
    else:
        total_score = sum(valid_scores)
        avg_score = total_score / len(valid_scores)
        score_range = max(valid_scores) - min(valid_scores)

        print(f"Scores processed: {valid_scores}")
        print(f"Total players: {len(valid_scores)}")
        print(f"Total score: {total_score}")
        print(f"Average score: {avg_score}")
        print(f"High score: {max(valid_scores)}")
        print(f"Low score: {min(valid_scores)}")
        print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
