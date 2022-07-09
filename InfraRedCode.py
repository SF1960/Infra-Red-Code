## Infrared code basics

import time
import os

DELAY_TIME = 0.5

time.sleep(DELAY_TIME);


try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO. This is probably because you need superuser. Try running again with 'sudo'.")
