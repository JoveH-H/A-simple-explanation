import random

r = 1.0  # 圆半径，假设为1
n = 300000  # 总投点数
count = 0  # 落到圆内投点数

# 投点x,y的范围
x_min, x_max = -r, r
y_min, y_max = -r, r

for i in range(0, n):

    # 在 [min, max] 范围内随机生成实数
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)

    # 落到圆内投点数+1
    if x * x + y * y <= r:
        count += 1

pi = (count / float(n)) * 4
print("pi is ", pi)
