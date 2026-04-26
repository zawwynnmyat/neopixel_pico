import time, random
from neopixel import Neopixel

numpix = 16
strip = Neopixel(numpix, 1, 1, "GRB")

while True:
    if random.random() < 0.1:
        flash_len = random.randint(3, numpix) 
        start = random.randint(0, numpix - flash_len)

        for i in range(flash_len):
            strip.set_pixel(start + i, (255, 255, 255))

        strip.show()
        time.sleep(0.05)

    for i in range(numpix):
        r, g, b = strip.get_pixel(i)
        strip.set_pixel(i, (int(r*0.6), int(g*0.6), int(b*0.6)))

    strip.show()
    time.sleep(0.05)