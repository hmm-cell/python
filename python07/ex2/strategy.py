from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy cannot be used by a creature."""


class BattleStrategy(ABC):
    """Abstract strategy for a creature's battle behavior."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return whether this strategy supports the creature."""

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Perform this strategy for the creature."""


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
