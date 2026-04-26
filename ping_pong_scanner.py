import time
from neopixel import Neopixel

numpix = 16
strip = Neopixel(numpix, 1, 1, "GRB")

pos = 0
direction = 1

def fade():
    for i in range(numpix):
        r, g, b = strip.get_pixel(i)
        strip.set_pixel(i, (int(r*0.6), int(g*0.6), int(b*0.6)))

while True:
    fade()

    strip.set_pixel(pos, (255, 0, 0))

    strip.show()
    time.sleep(0.03)

    pos += direction
    if pos == numpix - 1 or pos == 0:
        direction *= -1