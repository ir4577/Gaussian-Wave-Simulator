
#Entry point for the Gaussian Wave Simulator.
from src.constants import (
    INITIAL_POSITION,
    INITIAL_WAVENUMBER,
    INITIAL_WIDTH,
    NUM_POINTS,
    X_MAX,
    X_MIN,
)
from src.grid import Grid
from src.wavepacket import GaussianWavePacket
from src.potentials import FreeParticle,HarmonicPotential

def main() -> None:
    grid = Grid(
        xmin=X_MIN,
        xmax=X_MAX,
        num_points=NUM_POINTS,
    )
    packet = GaussianWavePacket(
        grid=grid,
        x0=INITIAL_POSITION,
        sigma=INITIAL_WIDTH,
        k0=INITIAL_WAVENUMBER,
    )
    potential = HarmonicPotential(grid, omega=0.5)
    print(potential.values)
    print(grid)
    print(packet)
    print(f"Norm = {packet.norm():.6f}")
if __name__ == "__main__":
    main()
