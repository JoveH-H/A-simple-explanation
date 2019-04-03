import matplotlib.pyplot as plt

Kp = 0.3  # 比例系数 调整系统的响应速度
Ki = 0.03  # 积分系数 主要解决达不到设定值的静态误差问题
Kd = 0.03  # 微分系数 主要解决积分项I存在导致系统的响应速度问题

goal = 100  # 目标值
output = [0, 0]  # 输出
bmp = 0  # 编码器反馈
err = [0, 0]  # 输出误差


def IncrementalPID_control():
    global bmp, output
    err[1] = err[0]  # 更新误差
    err[0] = goal - bmp

    output[0] = output[1] + Kp * err[0] + Ki * (err[0] + err[1]) + Kd * (err[0] - err[1])  # PID调节
    # 输出 = 基准 + P * 误差 + I * 累积误差 + D * 误差偏差

    bmp = output[0]  # 假设反馈等于现输出
    output[1] = output[0]  # 记录现输出


IncrementalTime = [0]  # 时间次数
IncrementalOutput = [0]  # 输出

for i in range(1, 20):  # 迭代
    IncrementalPID_control()  # 运算一次增量式PID
    IncrementalOutput.append(output[0])  # 添加输出结果
    IncrementalTime.append(i)  # 添加时间次数

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置正常显示中文
plt.plot(IncrementalTime, IncrementalOutput, label='output')  # 设置曲线数值
plt.xticks(IncrementalTime)  # 设置X轴坐标数值标识
plt.xlim(0)  # 设置X轴的范围（起始坐标）
plt.ylim(0)  # 设置Y轴的范围（起始坐标）
plt.xlabel('次数')  # 设置X轴的名字
plt.ylabel('输出')  # 设置Y轴的名字
plt.title("PID趋势图")  # 设置标题
plt.legend()  # 设置图例
plt.show()  # 显示图表
