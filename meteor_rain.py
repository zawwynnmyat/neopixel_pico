import time
from neopixel import Neopixel

numpix = 16
strip = Neopixel(numpix, 1, 1, "GRB")

def fade_all(fade_val):
    for i in range(numpix):
        r, g, b = strip.get_pixel(i)
        strip.set_pixel(i, (int(r*fade_val), int(g*fade_val), int(b*fade_val)))

while True:
    for i in range(numpix * 2):
        fade_all(0.75)

        if i < numpix:
            strip.set_pixel(i, (255, 255, 255))

        strip.show()
        time.sleep(0.03)