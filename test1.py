#%%
from pozyvec import draw, move, finish, init, noise, save
from math import sin, cos


width = 184
height = 268
init(width, height, stroke_width=0.1, stroke_color="white")


num_lines = 70
verts_per_line = 100
margin = 10

num_lines += margin * 2

for i in range(margin, num_lines - margin):
    y = width * i / num_lines
    move(0, y)
    for j in range(verts_per_line):
        x = height * j / verts_per_line
        y = y + noise([x, y], 0.007, 4, 3)

        x = x + sin(y * 0.1) * 10
        # y = cos(y * 0.1) * 100
        # y = cos(y)

        draw(x, y)


finish()
# save()

