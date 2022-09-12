#%%
from pozyvec import draw, move, finish, init, noise, save
from math import sin, cos, sqrt


width = 184
height = 268
init(width, height, stroke_width=0.3, stroke_color="white")


num_lines = 2
verts_per_line = 350
margin = 10

num_lines += margin * 2

# move(0, 0)

for j in range(verts_per_line):

    x = 0
    y = width * i / verts_per_line

    # move(x, y)
    for i in range(margin, num_lines - margin):
        x = height * j / (num_lines - margin * 3)

        vx = (x / width) * 2 - 1
        vy = (y / width) * 2 - 1

        a = 1.3

        x = (cos(vx * 3.14 * 2 / a) + sin(vy * 3.14 * 2 / a)) * width / 4 + width * 0.5
        y = (sin(vx * 3.14 * 2 / a) + cos(vy * 3.14 * 2 / a)) * width / 4 + width * 0.5

        # y = y + noise([x, y], 0.01, 10, 1)

        # y = sin((y * 2 * 3.14) / height) * height / 2 + height * 0.5
        # y = sin((y * 2 * 3.14) / height) * height / 2 + height * 0.5

        # vx = (x / width) * 2 - 1
        # vy = (y / height) * 2 - 1
        len = sqrt(vx*vx + vy*vy)
        # y *= 1.0 + len * 0.001

        # if len < 0.3:
        #     vx = vx / len
        #     vy = vy / len

        # vy = vy / len

        # ymag = (y / height) * 2 - 1

        # vy = cos(((y / width) * 2 - 1) * 3.14)
        # vy += ymag

        # vy =
        # vx *= 1.0 * (x / height) * 0.1

        # y = y + noise([x, y], 0.007, 4, 3)

        # x = x + sin(y * 0.1) * 100
        # y = cos(y * 0.1) * 100
        # y = cos(y)

        # x = vx * 80 + width / 2
        # y = vy * 80 + height / 2

        draw(x, y)


finish()
# save()
