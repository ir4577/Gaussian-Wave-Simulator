"""
potentials.py
Potential energy functions for one-dimensional quantum systems.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from src.grid import Grid


@dataclass(slots=True)
class Potential:
    """
    Base class for one-dimensional potentials.
    """

    grid: Grid
    values: np.ndarray = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.values = np.zeros(self.grid.num_points)


@dataclass(slots=True)
class FreeParticle(Potential):
    """
    Free particle.

    V(x) = 0
    """
pass

@dataclass(slots=True)
class HarmonicPotential(Potential):
    """
    Harmonic oscillator potential.

    V(x) = 1/2 mω²x²
    """

    omega: float = 1.0

    def __post_init__(self) -> None:

        x = self.grid.x

        self.values = (
            0.5
            * self.omega**2
            * x**2
        )
