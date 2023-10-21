"""Relation between a range of values and sound files"""
import os.path
import time

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

from . import pings


# I think these are misnamed ... I am not (that kind of) musician.
# I just need notes that don't clash and have a discernable higher/lower
# range.  Does C2 follow B2 or does C3 follow B2?
TONES = [# "C2", "D2", "E2", "F2", "G2",  # Too low to hear
         "A_3_piano", "B_3_piano", "C_3_pianoSTART",
         "D_3_piano", "E_3_piano", "F_3_piano", "G_3_piano",
         "A4", "B4", "C4", "D4", "E4", "F4", "G4",
         "A5", "B5", "C5"
         ]

_this_dir = os.path.dirname(__file__)
WAVE_DIR = os.path.join(_this_dir, "waves")

def wave_path(sound_name: str) -> str:
    """From a sound name like 'C3' to the corresponding file path"""
    suffixed = sound_name + ".wav"
    wave_file_path = os.path.join(WAVE_DIR, suffixed)
    absolute_path = os.path.abspath(wave_file_path)
    log.debug(f"{sound_name} => {absolute_path}")
    assert os.path.isfile(absolute_path), f"Did not find wave file'{wave_file_path}' ('{absolute_path}')"
    return absolute_path

WAVE_FILES = [wave_path(sound) for sound in TONES]

class AudioMap:
    def __init__(self,
                 utm_origin: tuple[int, int],
                 utm_ne_extent: tuple[int, int]):
        pings.init()
        self.origin = utm_origin
        self.extent = utm_ne_extent

    def plot_fire(self, easting: int, northing: int):
        self.plot_point(easting, northing, volume=0.2)

    def plot_cluster(self, easting: int, northing: int):
        self.plot_point(easting, northing, volume=0.5)

    def plot_point(self, easting: int, northing: int,
                   volume: float):
        x_origin, y_origin = self.origin
        x_extent, y_extent = self.extent
        x_wave = interpolate(easting, x_origin, x_extent)
        y_wave = interpolate(northing, y_origin, y_extent)
        pings.play(x_wave, volume)
        time.sleep(.05)
        pings.play(y_wave, volume)
        time.sleep(.10)

def interpolate(q: int, limit_low: int, limit_high: int) -> str:
    """Path to a wave file selected by interpolation
     of q between limit_low and limit_high.
    """
    assert limit_high > limit_low
    proportion = (q - limit_low) / (limit_high - limit_low)
    index = int(proportion * len(WAVE_FILES))
    index = max(0, min(len(WAVE_FILES)-1, index))
    log.debug(f"{q}[{limit_low}..{limit_high}] => {index}/{len(WAVE_FILES)}")
    wave = WAVE_FILES[index]
    log.debug(f"{q} => {wave}")
    return wave

def arpeggiate():
    """Janky ear test:  Are we interpolating sounds reasonably?"""
    pings.init()
    for i in range(30):
        wave = interpolate(i, 0, 30)
        print(wave)
        pings.play(wave)
        # input("Next")

