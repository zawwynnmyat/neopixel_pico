import time, math
from neopixel import Neopixel

numpix = 16
strip = Neopixel(numpix, 1, 1, "GRB")

offset = 0

while True:
    for i in range(numpix):
        brightness = (math.sin(i * 0.3 + offset) + 1) / 2
        color = (int(255 * brightness), 0, int(255 * (1 - brightness)))
        strip.set_pixel(i, color)

    strip.show()
    offset += 0.2
    time.sleep(0.05)