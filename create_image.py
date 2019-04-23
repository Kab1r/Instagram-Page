from PIL import Image, ImageDraw, ImageFont
import random

IMAGE_RES = 1080

FONT_PATH = './Proxima-Nova-Semibold.ttf'
# theme format is (background color, text color)
themes = [
    ('#ffffff', '#000000'),
    ('#000000', '#00857d'),
    ('#00857d', '#000000'),
    ('#ced8d8', '#ffffff'),
    ('#99a4a3', '#ffffff'),
]

def create_image(text):
    theme_num = random.randrange(0, themes.size)
    img = Image.new(
        'RGB',
        (IMAGE_RES,IMAGE_RES),
        color=themes[theme_num][0]
        )
    font = ImageFont.truetype(FONT_PATH, 24)

    drawer = ImageDraw.Draw(img)
    drawer.text(
        (50, 50),
        text,
        font=font,
        fill=themes[theme_num[1]]
        )
    return img