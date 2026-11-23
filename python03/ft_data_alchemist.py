import random


def main() -> None:
    names = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam',
    ]
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {names}")

    all_capitalized = [name.capitalize() for name in names]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized = [name for name in names if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")

    player_scores = {
        name: random.randint(1, 1000) for name in all_capitalized
    }
    print(f"Score dict: {player_scores}")

    avg_score = round(sum(player_scores.values()) / len(player_scores), 2)
    print(f"Score average is {avg_score}")

    high_scores = {
        name: score
        for name, score in player_scores.items()
        if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
