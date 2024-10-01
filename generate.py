from math import floor
import platform
import sys
from PIL import Image, ImageDraw, ImageFont

title = sys.argv[1]
author = sys.argv[2]
try:
        font = sys.argv[3]
except:
        font = "adobe-source-han-sans/SourceHanSansCN-Heavy.otf"

if platform.system() == "Windows":
        _font = "C:/Windows/Fonts/" + font
else:
        _font = "/usr/share/fonts/" + font

if len(title) < 8:
        titlesize = 55
elif len(title) < 16:
        titlesize = floor(8 / len(title) * 55)
else:
        titlesize = 25

image = Image.new('RGB', (695, 982), color = 0x6d7270)

draw = ImageDraw.Draw(image)

font = ImageFont.truetype(_font, titlesize);
font2 = ImageFont.truetype(_font, 20);
font3 = ImageFont.truetype(_font, 55 - len(author));

draw.text((90, 120), "Abstract studio studies in advanced joke                      ∞", font=font2, fill=0xfdfdfd)

titlearr = [title[i:i + 16] for i in range(0, len(title), 16)];
for i, group in enumerate(titlearr):
        draw.text((90, 250 + i * (titlesize + 20)), group, font=font, fill=0xfdfdfd)

draw.text((90, 400), author, font=font3, fill=(203, 47, 40))

draw.line((250, 1000, 700, 550), fill='white', width=15)
draw.line((280, 1000, 710, 570), fill='red', width=40)
draw.line((340, 1000, 710, 630), fill='red', width=40)
draw.line((378, 1000, 710, 668), fill='white', width=15)

image.save("a.png")

image.show()
