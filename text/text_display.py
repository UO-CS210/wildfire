"""A textual "display" of fire map data."""
import config


class TextMap:
    """Textual output with interface compatible with visual and audio displays."""

    def __init__(self, verbosity=config.DISPLAY_FIRES_CONCISE):
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
        if self.verbosity == config.DISPLAY_FIRES_VERBOSE:
            print(f"Fire at {x}, {y} ({easting}, {northing})")
        elif self.verbosity == config.DISPLAY_FIRES_CONCISE:
            print(f"Fire at {x}, {y}")
        elif self.verbosity == config.DISPLAY_CLUSTERS_ONLY:
            pass

    def plot_cluster(self, easting: int, northing: int):
        if easting == 0 and northing == 0:
            # Special case for empty cluster
            print(f"Empty cluster")
        else:
            x, y = self.to_grid(easting, northing)
            print(f"Cluster at {x}, {y}")

    def move_cluster(self,
                     old_pos: tuple[int, int],
                     new_pos: tuple[int, int]):
        """Depict movement of a cluster"""
        if old_pos == (0, 0):
            return

        old_e, old_n = old_pos
        old_x, old_y = self.to_grid(old_e, old_n)
        if new_pos == (0, 0):
            print(f"Cluster at {old_x}, {old_y} emptied")
            return
        if old_pos == new_pos:
            print(f"Cluster at {old_x}, {old_y} unchanged")

        new_e, new_n = new_pos
        new_x, new_y = self.to_grid(new_e, new_n)
        if (new_x, new_y) == (old_x, old_y):
            print(f"Cluster at {old_x}, {old_y} nudged slightly")
        else:
            print(f"Cluster at {old_x}, {old_y} moved to {new_x}, {new_y}")

