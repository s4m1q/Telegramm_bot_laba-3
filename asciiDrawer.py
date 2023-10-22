from PIL import Image, ImageDraw

import math

CHARS = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ALPHABET_LENGTH = len(CHARS)
INTERVAL = ALPHABET_LENGTH / 256
SCALE = 0.13
CHAR_WIDTH = 10
CHAR_HEIGHT = 10


def create(path):
    image = Image.open(path)

    width, height = image.size
    image = image.resize((int(SCALE * width), int(SCALE * height * (CHAR_WIDTH / CHAR_HEIGHT))),
                         Image.NEAREST)

    width, height = image.size
    pixels = image.load()

    outputImage = Image.new('RGB', (CHAR_WIDTH * width, CHAR_HEIGHT * height), color=(0, 0, 0))
    drawer = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r, g, b = pixels[j, i]
            avrg = int(r / 3 + g / 3 + b / 3)
            pixels[j, i] = (avrg, avrg, avrg)

            drawer.text((j * CHAR_WIDTH, i * CHAR_HEIGHT), CHARS[math.floor(avrg * INTERVAL)], fill=(r, g, b))

    outputImage.save('./images/output.png')
