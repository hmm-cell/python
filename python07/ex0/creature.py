from abc import ABC, abstractmethod


class Creature(ABC):
    """Base class for all creatures."""

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """Return the creature's attack message."""

    def describe(self) -> str:
        """Return the standard creature description."""
        return f"{self.name} is a {self.creature_type} type Creature"


class CreatureFactory(ABC):
    """Abstract factory for a creature family."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base creature of this family."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved creature of this family."""
