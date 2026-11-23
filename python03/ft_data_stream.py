import random
import typing

PLAYERS = ["bob", "alice", "dylan", "charlie"]
ACTIONS = ["run", "move", "grab", "sleep", "eat", "climb", "swim", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    event_list: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        random_index = random.randint(0, len(event_list) - 1)
        yield event_list.pop(random_index)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator = gen_event()

    for i in range(1000):
        player, action = next(generator)
        print(f"Event {i}: Player {player} did action {action}")

    ten_tups: list[tuple[str, str]] = []
    for _ in range(10):
        ten_tups.append(next(generator))

    print(f"Built list of 10 events: {ten_tups}")

    for player, action in consume_event(ten_tups):
        print(f"Got event from list: ('{player}', '{action}')")
        print(f"Remains in list: {ten_tups}")


if __name__ == "__main__":
    main()
