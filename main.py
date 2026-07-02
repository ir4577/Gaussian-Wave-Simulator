from src.constants import NUM_POINTS, X_MIN, X_MAX
from src.grid import Grid
from src.wavepacket import GaussianWavePacket

def main() -> None:
    """
    Run the Gaussian wave packet simulation.
    """

    grid = Grid(
        xmin=-X_MIN,
        xmax=X_MAX,
        num_points=NUM_POINTS,
    )
    print(grid)

    packet = GaussianWavePacket(
        grid=grid,
        x0=-3.0,
        sigma=0.5,
        k0=5.0,
    )

    print(packet)


if __name__ == "__main__":
    main()
