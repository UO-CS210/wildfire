"""Very simple sonification functions using PyGame audio.
Sounds should be in the "waves" directory.
"""

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

ENABLED = True
try:
    import pygame
    log.debug("Pygame loaded for sonification")
except:
    ENABLED = False

if ENABLED:
    import time
    import pygame.mixer as mixer

import os
THIS_DIR = os.path.abspath(os.path.dirname(__file__))

def init():
    if ENABLED:
        pygame.init()
        mixer.init()
    else:
        log.warning("Sonification disabled because pygame not installed."
                  "\nTry 'pip install pygame'.")


def play(path: str, volume=0.4):
    """Play a sound, briefly"""
    if not ENABLED:
        return
    sound = mixer.Sound(path)
    sound.set_volume(volume)
    log.debug(f"Sound is {sound}")
    chan = sound.play()
    log.debug(f"Channel is {chan}")
    # Polling loop; can we do better?
    while chan.get_busy():
        time.sleep(0.01)




