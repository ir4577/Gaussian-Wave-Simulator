"""
wavepacket.py

Defines Gaussian wave packets for one-dimensional quantum simulations.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from src.grid import Grid


@dataclass(slots=True)
class GaussianWavePacket:
    """
    grid: Computational grid.
    x0: Initial position.
    sigma: Spatial width of the packet.
    k0: Initial wave number.
    """

    grid: Grid
    x0: float
    sigma: float
    k0: float

    def __post_init__(self) -> None:
        """Construct and normalize the wavefunction."""

        self._initialize()
        self.normalize()

    def _initialize(self) -> None:
        """Construct the initial Gaussian wavefunction."""

        x = self.grid.x

        self.psi = (
            np.exp(-((x - self.x0) ** 2) / (4.0 * self.sigma ** 2))
            * np.exp(1j * self.k0 * x)
        )

    def normalize(self) -> None:
        """Normalize the wavefunction."""

        norm = np.sqrt(
            np.sum(np.abs(self.psi) ** 2) * self.grid.dx
        )

        self.psi /= norm

    def norm(self) -> float:
        """Return the total probability."""

        return float(
            np.sum(np.abs(self.psi) ** 2) * self.grid.dx
        )

    @property
    def probability_density(self) -> np.ndarray:
        """Return |ψ|²."""

        return np.abs(self.psi) ** 2

    def copy(self) -> np.ndarray:
        """Return a copy of the wavefunction."""

        return self.psi.copy()

    def __repr__(self) -> str:
        return (
            "GaussianWavePacket("
            f"x0={self.x0}, "
            f"sigma={self.sigma}, "
            f"k0={self.k0})"
        )
