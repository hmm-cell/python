from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Capability that allows a creature to heal."""

    @abstractmethod
    def heal(self) -> str:
        """Return the healing action message."""


class TransformCapability(ABC):
    """Capability that allows a creature to change form."""

    @abstractmethod
    def transform(self) -> str:
        """Return the transformation message."""

    @abstractmethod
    def revert(self) -> str:
        """Return the reverted-form message."""
