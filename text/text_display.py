"""A textual "display" of fire map data."""
import config

# verbosity levels
DISPLAY_CLUSTERS_ONLY = 1
DISPLAY_FIRES_CONCISE = 3
DISPLAY_FIRES_VERBOSE = 5

class TextMap:
    """Textual output with interface compatible with visual and audio displays."""

    def __init__(self, verbosity=DISPLAY_FIRES_CONCISE):
        self.verbosity = verbosity

    def to_grid(self, easting: int, northing: int) -> tuple[int, int]:
        """Compress UTM coordinates to a more readable scale of grid points"""
        x = int(config.TEXT_COORD_GRID
                * (easting - config.BASEMAP_ORIGIN_EASTING)
                / (config.BASEMAP_EXTENT_EASTING - config.BASEMAP_ORIGIN_EASTING))
        y = int(config.TEXT_COORD_GRID
                * (northing - config.BASEMAP_ORIGIN_NORTHING)
                / (config.BASEMAP_EXTENT_NORTHING - config.BASEMAP_ORIGIN_NORTHING))
        return x, y

    def plot_fire(self, easting: int, northing: int):
        x, y = self.to_grid(easting, northing)
        if self.verbosity == DISPLAY_FIRES_VERBOSE:
            print(f"Fire at {x}, {y} ({easting}, {northing})")
        elif self.verbosity == DISPLAY_FIRES_CONCISE:
            print("Fire at {x}, {y}")
        elif self.verbosity == DISPLAY_CLUSTERS_ONLY:
            pass

    def plot_cluster(self, easting: int, northing: int):
        x, y = self.to_grid(easting, northing)
        print(f"Cluster at {x}, {y}")
