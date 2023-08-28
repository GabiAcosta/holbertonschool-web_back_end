#!/usr/bin/env python3
"""
Multiplier Function Factory

This module defines a function factory that creates multiplier functions.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function with the given multiplier."""
    def multiplier_function(x: float) -> float:
        """The multiplier function."""
        return x * multiplier
    return multiplier_function
