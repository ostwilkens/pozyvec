# #%%
# import axi
# import time
# import random
# import math

# device = axi.Device()

# def up():
#     device.pen_up()

# def down():
#     device.pen_down()

# device.command('SP', 1, 0.01)

# device.pen_up()
# device.enable_motors()
# time.sleep(0.2)
# points = []
# points.append((0, 0))
# for i in range(10):
#     while True:
#         x = random.random() * 11
#         y = random.random() * 8.5
#         r = random.random() * 4
#         if x - r < 0 or x + r > 11:
#             continue
#         if y - r < 0 or y + r > 8.5:
#             continue
#         break
#     rotation = random.random() * 2 * math.pi
#     c = circle(x, y, r, 90, rotation)
#     if random.random() < 0.5:
#         c = list(reversed(c))
#     points.extend(c)
# points.append((0, 0))
# device.run_path(points)
# device.wait()
# device.disable_motors()

# paths = [[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]]
# drawing = axi.Drawing(paths)
# drawing = drawing.rotate_and_scale_to_fit(10.55, 7.244, step=90)
# axi.draw(drawing)

#%%
from ctypes.wintypes import SHORT
import time
from pyaxidraw import axidraw

ad = axidraw.AxiDraw()
ad.interactive()
connected = ad.connect()
print(connected)

#%%
# ad.penup()
# ad.goto(10, 10)
# ad.penup()
ad.goto(0, 0)


#%%
from random import random

# # https://axidraw.com/doc/py_api/
# ad.options.units = 2  # millimeters
# ad.options.const_speed = False  # True or False (False)
# ad.options.model = 2  # AxiDraw V3/A3
# ad.options.pen_pos_down = 50  # integers from 0 to 100 (40)
# ad.options.pen_pos_up = 62  # integers from 0 to 100 (60)

# ad.options.speed_pendown = 25  # integers from 1 to 110 (25)
# ad.options.speed_penup = 75  # integers from 1 to 110 (75)
# ad.options.accel = 75  # integers from 1 to 100 (75)
# ad.options.pen_rate_lower = 50  # integers from 1 to 100 (50)
# ad.options.pen_rate_raise = 75  # integers from 1 to 100
# ad.options.pen_delay_down = 0  # -500 to 500 (0)
# ad.options.pen_delay_up = 0  # -500 to 500 (0)
# ad.update()

#%%

PAPER_WIDTH = 268
PAPER_HEIGHT = 184
MARGIN = 10
WIDTH = PAPER_WIDTH - MARGIN * 2
HEIGHT = PAPER_HEIGHT - MARGIN * 2
LONGEST_EDGE = max(WIDTH, HEIGHT)
SHORTEST_EDGE = min(WIDTH, HEIGHT)
OFFSET_X = MARGIN
OFFSET_Y = MARGIN
CENTER_X = PAPER_WIDTH / 2
CENTER_Y = PAPER_HEIGHT / 2
RATIO_X = WIDTH / SHORTEST_EDGE
RATIO_Y = HEIGHT / SHORTEST_EDGE


def up():
    ad.penup()


def down():
    ad.pendown()


# def goto(x, y):
#     ad.goto(x, y)


# 0 -> WIDTH / 2 + OFFSET_X


def go(x, y):
    center_x = WIDTH / 2 + OFFSET_X
    center_y = HEIGHT / 2 + OFFSET_Y

    ax = center_x + x * SHORTEST_EDGE / 2
    ay = center_y + y * SHORTEST_EDGE / 2

    ad.goto(ax, ay)

    # ad.goto((x / 2 + 0.5) * SHORTEST_EDGE + OFFSET_X, (y / 2 + 0.5) * SHORTEST_EDGE + OFFSET_Y)


def rand():
    return random() * 2 - 1


import numpy as np

for x in np.arange(-RATIO_X, RATIO_X, 0.25):
    for y in np.arange(-RATIO_Y, RATIO_Y, 0.25):
        go(x, y)
        down()

        for j in range(0, 12):
            go(x + rand() * 0.1, y + rand() * 0.1)

        up()

#%%
ad.disconnect()