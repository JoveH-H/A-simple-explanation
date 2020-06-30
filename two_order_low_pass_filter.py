import numpy as np
import matplotlib.pyplot as plt

delta_t = 0.001                             # 采集间隔时间
end_t = 10                                  # 时间长度
time_t = int(end_t / delta_t)               # 采样次数
t = np.arange(0, end_t, delta_t)            # 设置时间数组

x = 1 * np.sin(t*2) # 实际真实信号

v_var = 0.05 # 测量噪声的方差
v_noise = np.round(np.random.normal(0, v_var, time_t), 3)  # 创建高斯噪声，精确到小数点后三位

X = np.mat([[0], [0]])   # 定义预测优化值的初始状态 
Y_mat = np.zeros(time_t) # 初始化记录系统预测优化值的列表
v = np.mat(v_noise)      # 定义测量噪声
z = x + v                # 定义测量值（假设测量值=实际状态值+噪声）
fc = 10                  # 截止频率 Hz
Wc = 2 * np.pi * fc      # 开环截止频率
Tsw = delta_t            # 采样时间
Zeta = 0.707             # 阻尼比

B0 = Wc * Wc * Tsw * Tsw
A0 = B0 + 4 * Zeta * Wc * Tsw + 4
A1 = 2 * B0 - 8
A2 = B0 - 4 * Zeta * Wc * Tsw + 4

LPF2_X = [0, 0, 0]
LPF2_Y = [0, 0, 0]

for i in range(time_t):
    LPF2_X[0] = z[0, i]
    LPF2_Y[0] = (B0 * LPF2_X[0] + 2 * B0 * LPF2_X[1] + B0 * LPF2_X[2] - A1 * LPF2_Y[1] - A2 * LPF2_Y[2]) / A0
    LPF2_X[2] = LPF2_X[1]
    LPF2_X[1] = LPF2_X[0]
    LPF2_Y[2] = LPF2_Y[1]
    LPF2_Y[1] = LPF2_Y[0]
    # 记录系统的过滤预测值
    Y_mat[i] = LPF2_Y[0]

plt.rcParams['font.sans-serif'] = ['SimHei']    # 设置正常显示中文
plt.plot(z.T, "r--", label='测量值')             # 设置曲线数值
plt.plot(x, "b", label='实际状态值')
plt.plot(Y_mat, "g", label='过滤预测值')
plt.xlabel("时间")                               # 设置X轴的名字
plt.ylabel("信号")                               # 设置Y轴的名字
plt.title("二阶低通滤波器示意图")                 # 设置标题
plt.legend()                                    # 设置图例
plt.show()                                      # 显示图表
