#%%
from pozyvec import draw, move, finish, init, noise, save
from math import floor, sqrt

width = 184
height = 264 - 25
init(width, height, 3)

target_step_size_x = 140
target_step_size_y = 140
step_size_x = width / floor(width / target_step_size_x)
step_size_y = height / floor(height / target_step_size_y)
steps_x = floor(width / step_size_x)
steps_y = floor(height / step_size_y)
repels = []
x = 0
y = 0

for a in range(steps_x):
    for b in range(steps_y):
        ox = a * step_size_x + step_size_x / 2
        oy = b * step_size_y + step_size_y / 2
        ocell = noise([x, y * 3], 0.01, 100, 3)
        m = 5
        for j in range(1000):
            x = (width + ox) / 4 + noise([0, j * 10], 0.05, 100, 3)
            y = (height + oy) / 4 + noise([j * 10, 0], 0.05, 200, 3)
            vx = 0
            vy = 0
            dist = 1
            move(x * 2, y * 2)
            for i in range(1000):
                coll = True
                k = 0
                while k < 100 and coll:
                    k += 1
                    vx -= noise([x, y + j * 666 + k * 666 + ocell], 0.01, 20, 1)
                    vy -= noise([y, x + j * 666 + k * 666 + ocell], 0.01, 10, 3)
                    len = sqrt(vx * vx + vy * vy) / (1 - dist * 0.08)
                    vx /= len
                    vy /= len
                    dist = (
                        sqrt(
                            (x + vx - width / 4) * (x + vx - width / 4)
                            + (y / 2 + vy - height / 8) * (y / 2 + vy - height / 8)
                        )
                        - noise([x / 40, y / 40, ocell], 0.3, 50, 1)
                        + 35
                    )
                    cell = floor(x + vx) * width + floor(y + vy)
                    outside_bounds = (
                        x + vx < m
                        or x + vx > width - m
                        or y + vy < m
                        or y + vy > height - m
                    )
                    outside_circle = dist > 50
                    coll = cell in repels or outside_circle or outside_bounds
                if not coll:
                    x += vx
                    y += vy
                    draw(x * 2, y * 2)
                    repels.append(cell)
                else:
                    break

finish()
