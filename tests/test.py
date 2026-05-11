from playsound import playsound
import sys
import time
from pathlib import Path
from playsound import playsound

import pygame
import time
base = Path(__file__).resolve().parent
pygame.mixer.init()
planarcadia = base.parent / "data" / "assets" / "planarcadia.mp3"
pygame.mixer.music.load(str(planarcadia))
pygame.mixer.music.set_volume(0.3)

pygame.mixer.music.play(-1)

while True:
    time.sleep(1)