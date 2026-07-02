#Global constants and default simulation parameters.
from __future__ import annotations
# Physical Constants (Natural Units)
HBAR: float = 1.0
MASS: float = 1.0
# Spatial Grid
X_MIN: float = -20.0
X_MAX: float = 20.0
NUM_POINTS: int = 2048
# Time Evolution
DT: float = 0.005
TOTAL_TIME: float = 5.0
# Initial Gaussian Wave Packet
INITIAL_POSITION: float = -8.0
INITIAL_WIDTH: float = 1.0
INITIAL_WAVENUMBER: float = 5.0
