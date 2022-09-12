#%%
from rembg import remove
from PIL import Image, ImageChops
import cv2
import numpy as np
import os


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


cap = cv2.VideoCapture(0)

cv2_img = None
for i in range(5):
    ret_val, cv2_img = cap.read()

cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(cv2_img)
pil_img = remove(pil_img)
pil_img = trim(pil_img)
new_image = Image.new("RGBA", pil_img.size, "WHITE")
new_image.paste(pil_img, (0, 0), pil_img)
new_image.convert("RGB")


new_image.save("output.bmp")
os.system("potrace -s --tight < output.bmp > output.svg")
new_image


#%%

from pozyvec import draw, move, finish, init, noise, save
from math import sin, cos, sqrt, floor

np_img = np.array(new_image)

div_a = 4

width = floor(np_img.shape[1] / div_a)
height = floor(np_img.shape[0] / div_a)
# init(width, height, stroke_width=0.3, stroke_color="white")
init(width, height, display_inline=True)

div_b = 1


for a in range(floor(height / div_b)):
    y = a * div_b
    # move(0, y)
    for b in range(floor(width / div_b)):
        x = b * div_b

        p = np_img[(height - y - 1) * div_a][x * div_a].astype(np.int32)
        v = (p[0] + p[1] + p[2]) / 3
        if v < 128:
            draw(x, y)
        else:
            move(x, y)


finish()
# save()

#%%
import os

print(os.name)
