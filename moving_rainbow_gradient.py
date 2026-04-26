import time
from neopixel import Neopixel

numpix = 16
strip = Neopixel(numpix, 1, 1, "GRB")

offset = 0

while True:
    for i in range(numpix):
        hue = (i * 65536 // numpix + offset) % 65536
        color = strip.colorHSV(hue, 255, 150)
        strip.set_pixel(i, color)

    strip.show()
    offset += 500
    time.sleep(0.02)