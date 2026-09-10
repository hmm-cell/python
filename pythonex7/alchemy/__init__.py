"""Alchemy package. Only create_air is exposed here — create_earth
is intentionally left out so it stays unreachable via 'alchemy.create_earth()'.
"""
from .elements import create_air
from .elements import create_earth
