from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    healing = HealingCreatureFactory()
    base = healing.create_base()
    evolved = healing.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

    print("\nTesting Creature with transform capability")
    transforming = TransformCreatureFactory()
    base = transforming.create_base()
    evolved = transforming.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    main()
