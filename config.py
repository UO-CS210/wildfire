"""Configuration file, wildfires k-means clustering.

This should be all the constants that must be changed to
substitute a different data set and base map for the
provided Oregon wildfires data set and Oregon base map.
See also the README file in the data directory for
notes on obtaining suitable datasets and basemaps, and program
add_utm.py for augmenting a data set with UTM coordinates.
"""

####
#   Settings for computation
####

FIRE_DATA_PATH = "data/fire_five_utm.csv"
# We can read just part of the data file to speed
# debugging
N_RECORDS = 20
# How many clusters should we try to make?
N_CLUSTERS = 3
# How long will we allow the algorithm to run?
# (It will usually end much sooner)
MAX_ITERATIONS = 20

####
# Settings for display
####

BASEMAP_PATH = "data/Oregon.png"

DISPLAY_VISUAL = True     # Make a visual display of the data
DISPLAY_AUDIO = True      # Make an audio display of the data (requires Pygame)
DISPLAY_TEXT = True       # Print the data (with verbosity level below)
TEXT_VERBOSITY = 5  # Verbose
TEXT_COORD_GRID = 10   #  Compress coordinates to 0..TEXT_COORD_GRID

BASEMAP_SIZE = (1024, 783)
# Origin    (-124.9, 41.8) =  342151, 4629315 10T
# NE corner (-116.3, 46.5) = 1014041, 5171453 10T
BASEMAP_ORIGIN_EASTING = 342151
BASEMAP_ORIGIN_NORTHING = 4629315
BASEMAP_EXTENT_EASTING = 1014041
BASEMAP_EXTENT_NORTHING = 5171453
BASEMAP_WIDTH_UTM = BASEMAP_EXTENT_EASTING - BASEMAP_ORIGIN_EASTING
BASEMAP_HEIGHT_UTM =  BASEMAP_EXTENT_NORTHING - BASEMAP_ORIGIN_NORTHING

FIRE_MARK_POINTS = 5
FIRE_MARK_COLOR = "red"

CLUSTER_MARK_POINTS = 15