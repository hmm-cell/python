import random


def gen_player_achievements(pool: list[str]) -> set[str]:
    num_achievements = random.randint(1, len(pool))
    chosen = random.sample(pool, num_achievements)
    return set(chosen)


def main() -> None:
    game_pool = [
        'Crafting Genius',
        'World Savior',
        'Master Explorer',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Strategist',
        'Unstoppable',
        'Speed Runner',
        'Survivor',
        'Treasure Hunter',
        'First Steps',
        'Sharp Mind',
        'Hidden Path Finder',
    ]

    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements(game_pool)
    bob = gen_player_achievements(game_pool)
    charlie = gen_player_achievements(game_pool)
    dylan = gen_player_achievements(game_pool)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct = set.union(alice, bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")

    common = set.intersection(alice, bob, charlie, dylan)
    print(f"Common achievements: {common}")

    only_alice = set.difference(alice, set.union(bob, charlie, dylan))
    only_bob = set.difference(bob, set.union(alice, charlie, dylan))
    only_charlie = set.difference(charlie, set.union(alice, bob, dylan))
    only_dylan = set.difference(dylan, set.union(alice, bob, dylan))

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    full_pool_set = set(game_pool)
    print(f"Alice is missing: {set.difference(full_pool_set, alice)}")
    print(f"Bob is missing: {set.difference(full_pool_set, bob)}")
    print(f"Charlie is missing: {set.difference(full_pool_set, charlie)}")
    print(f"Dylan is missing: {set.difference(full_pool_set, dylan)}")


if __name__ == "__main__":
    main()
