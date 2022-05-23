#%%
from pozyvec import draw, move, finish, init, noise, save


width = 268
height = 184
init(width, height)


num_lines = 100
verts_per_line = 100

for i in range(num_lines):
    x = width * i / num_lines
    move(x, 0)
    for j in range(verts_per_line):
        y = height * j / verts_per_line
        x = x + noise([x, y], 0.005, 2, 5)
        draw(x, y)


finish()
# save()

