"""Display for geographic clustering of wildfire data.
Includes visual display, audio display, each optional.

Visual display uses Python's TkInter visual via Zelle's visual module,
and is "self-contained" in the sense nothing else needs to be installed.
Audio display uses PyGame, which must be installed from PyPi, typically
with "pip".
"""
from typing import Optional

import config
import visual.visual_map as visual
import audio.wave_map as audio
import text.text_display as text

class Display:
    """Whatever we need to track for displays of all kinds,
    including graphical, audio, and text.
    """
    def __init__(self,
                 display_visual=True,
                 display_audio=True,
                 display_text=True):

        self.visual: Optional[visual.VisualMap] = None
        self.symbols = []  # Only for visual at this time
        self.positions = []  # For any kind of point
        self.kinds = []  # Each kind of point
        if display_visual:
            self.visual =  visual.VisualMap(config.BASEMAP_PATH,
                                            config.BASEMAP_SIZE,
                                            (config.BASEMAP_ORIGIN_EASTING, config.BASEMAP_ORIGIN_NORTHING),
                                            (config.BASEMAP_EXTENT_EASTING, config.BASEMAP_EXTENT_NORTHING))

        self.audio: Optional[audio.AudioMap] = None
        if display_audio:
            self.audio = audio.AudioMap(
                (config.BASEMAP_ORIGIN_EASTING, config.BASEMAP_ORIGIN_NORTHING),
                (config.BASEMAP_EXTENT_EASTING, config.BASEMAP_EXTENT_NORTHING))

        self.textual: Optional[text.TextMap] = None
        if display_text:
            self.textual = text.TextMap(verbosity=config.TEXT_VERBOSITY)

    def plot_fire(self, easting: int, northing: int) -> int:
        index = len(self.symbols)
        self.positions.append((easting, northing))
        self.kinds.append("fire")
        if self.visual:
            self.symbols.append(self.visual.plot_fire(easting,northing))
        if self.audio:
            self.audio.plot_fire(easting, northing)
        if self.textual:
            self.textual.plot_fire(easting, northing)

    def mark_cycle(self):
        """Indicate that we have begun an iteration of
        clustering.  Indication varies by display mode.
        """
        if self.visual:
            self.visual.mark_cycle()
        if self.audio:
            self.audio.mark_cycle()
        if self.textual:
            self.textual.mark_cycle()


    def plot_cluster(self, easting: int, northing: int) -> int:
        index = len(self.symbols)
        self.positions.append((easting, northing))
        self.kinds.append("cluster")
        if self.visual:
            self.symbols.append(self.visual.plot_cluster(easting,northing))
        if self.audio:
            self.audio.plot_cluster(easting, northing)
        if self.textual:
            self.textual.plot_cluster(easting, northing)
        return len(self.symbols) - 1


    def move_symbol(self, symbol: int, to_location: tuple[int, int]):
        easting, northing = to_location
        if self.visual:
            graphic = self.symbols[symbol]
            self.visual.move_point(graphic, (easting, northing))
        if self.audio:
            self.audio.plot_cluster(easting, northing)
        if self.textual:
            self.textual.move_cluster(self.positions[symbol],
                                      (easting, northing))
        self.positions[symbol] = (easting, northing)

    def show_connections(self,
                         symbols: list[int],
                         connected_to: list[list[tuple[int, int]]]
                         ):
        for i in range(len(symbols)):
            sym_idx = symbols[i]
            if self.visual:
                hub = self.symbols[sym_idx]
                self.visual.show_connections(hub, connected_to[i])
            if self.audio:
                pass  # Don't know how to do this with sound
            if self.textual:
                hub = self.positions[i]
                self.textual.show_connections(hub, connected_to[i])
