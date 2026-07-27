import random
import typing

PLAYERS = ["bob", "alice", "dylan", "charlie"]
ACTIONS = ["run", "move", "grab", "sleep", "eat", "climb", "swim", "release"]

def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player: random.choice(PLAYERS)
        action: random.choice(ACTIONS)
        yield(player, action)

generator = get_event()
    
    
