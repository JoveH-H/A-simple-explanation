import random

n = 300000  # 总投点数
count = 0  # 位于曲线之下的投点数

# 投点x,y的范围
x_min, x_max = 0.0, 1.0
y_min, y_max = 0.0, 1.0

for i in range(0, n):

    # 在[min, max]范围内随机生成实数
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)

    # 位于曲线之下的投点数+1
    if x * x * x >= y:
        count += 1

# 所求的积分值即为曲线下方的面积与正方形面积1的比
result = count / float(n)
print("result is ", result)
