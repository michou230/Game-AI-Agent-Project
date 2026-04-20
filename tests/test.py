from playsound import playsound
import sys
import time
from pathlib import Path
from playsound import playsound

base = Path(__file__).resolve().parent
audio = base.parent / "data" / "assets" / "AudioCutter_sundayyy.mp3"

def slow(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


playsound(str(audio), block = False)
time.sleep(2.7)
slow("\nAll the work of creation has been completed..")
time.sleep(1.97)
slow("The inevitable day has arrived..")
time.sleep(1.90)
slow("The Embryo of Philosophy..")
time.sleep(1.4)
slow("WILL RESHAPE FOR US ALL OF REALITY!\n")
time.sleep(4)
print("The boss has transformed to its second phase!\n")