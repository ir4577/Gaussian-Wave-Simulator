
#Defines the one-dimensional computational grid.
from __future__ import annotations
from dataclasses import dataclass,field
import numpy as np
@dataclass(slots=True)
class Grid:
    """
    One-dimensional spatial grid.

    Parameters
    ----------
    xmin:  Left boundary.
    xmax:  Right boundary.
    num_points: Number of grid points.
    """

    xmin: float
    xmax: float
    num_points: int


    x: np.ndarray = field(init=False, repr=False)
    k: np.ndarray = field(init=False, repr=False)
    dx: float = field(init=False)

    def __post_init__(self) -> None:
        """
        Construct spatial and momentum grids.
        """

        self.x = np.linspace(
            self.xmin,
            self.xmax,
            self.num_points,
            endpoint=False,
        )

        self.dx = self.x[1] - self.x[0]

        self.k = 2.0 * np.pi * np.fft.fftfreq(
            self.num_points,
            d=self.dx,
        )

    @property
    def length(self) -> float:
        """Length of the computational domain."""

        return self.xmax - self.xmin

    def __repr__(self) -> str:
        return (
            "Grid("
            f"xmin={self.xmin}, "
            f"xmax={self.xmax}, "
            f"num_points={self.num_points}, "
            f"dx={self.dx:.5f})"
        )
