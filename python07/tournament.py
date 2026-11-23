from ex0.creature import CreatureFactory
from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print(f"*** Tournament ***\n{len(opponents)} opponents involved")
    creatures = [(factory.create_base(), strategy)
                 for factory, strategy in opponents]

    for first_index in range(len(creatures)):
        for second_index in range(first_index + 1, len(creatures)):
            first, first_strategy = creatures[first_index]
            second, second_strategy = creatures[second_index]

            print("\n* Battle *")
            print(first.describe())
            print(" vs.")
            print(second.describe())
            print(" now fight!")

            try:
                if not first_strategy.is_valid(first):
                    strategy_name = (
                        "aggressive"
                        if isinstance(first_strategy, AggressiveStrategy)
                        else "defensive"
                        if isinstance(first_strategy, DefensiveStrategy)
                        else "normal"
                    )
                    raise InvalidStrategyError(
                        f"Invalid Creature '{first.name}' "
                        f"for this {strategy_name} strategy"
                    )
                if not second_strategy.is_valid(second):
                    strategy_name = (
                        "aggressive"
                        if isinstance(second_strategy, AggressiveStrategy)
                        else "defensive"
                        if isinstance(second_strategy, DefensiveStrategy)
                        else "normal"
                    )
                    raise InvalidStrategyError(
                        f"Invalid Creature '{second.name}' "
                        f"for this {strategy_name} strategy"
                    )
                first_strategy.act(first)
                second_strategy.act(second)
            except InvalidStrategyError as error:
                print(
                    "Battle error, aborting tournament: "
                    f"{error}"
                )
                return


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("  [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ])

    print("\nTournament 1 (error)")
    print("  [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ])

    print("\nTournament 2 (multiple)")
    print(
        "  [ (Aquabub+Normal), (Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )
    battle([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])


if __name__ == "__main__":
    main()
