import numpy as np


def sigmoid(z):  # 激活函数
    a = 1 / (1 + np.exp(-z))
    return a


def d_sigmoid(a):  # 激活函数的导数
    return a * (1 - a)


X = np.array(
    [[0.1, 1.1, 0.5], [1.1, 0.1, 1.5], [0.3, 1.4, 0.7], [1.4, 0.1, 1.1], [0.5, 1.8, 0.9], [1.0, 0.6, 1.8],
     [0.7, 1.9, 0.1], [1.1, 0.2, 1.3], [0.9, 2.1, 0.8], [1.5, 0.1, 1.8], [0.1, 1.8, 0.6], [1.5, 0.3, 1.9],
     [0.3, 1.7, 0.2], [1.7, 0.4, 1.5], [0.5, 1.1, 0.3], [1.6, 0.6, 1.8], [0.7, 1.5, 0.2], [1.5, 0.8, 1.2],
     [0.9, 1.9, 0.5], [1.9, 1, 2.6]])
X = X.T  # 转置X

y = np.array(
    [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]])

m = X.shape[1]
X = (X - np.mean(X)) / np.linalg.norm(X, ord=2, axis=1, keepdims=True)  # 归一化输入

w1 = np.random.randn(3, 4) * np.sqrt(1 / 3)  # 权重初始化
b1 = np.random.randn(4, 1)
w2 = np.random.randn(4, 1) * np.sqrt(1 / 4)
b2 = np.random.randn(1, 1)
alpha = 1  # 学习效率
lambd = 0.03  # 正则化参数

for i in range(0, 500):  # 迭代500次
    # 向前传播
    Z1 = np.dot(w1.T, X) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(w2.T, A1) + b2
    A2 = sigmoid(Z2)
    # 反向传播
    dz2 = (A2 - y)
    dw2 = np.dot(A1, dz2.T) / m + lambd * w2 / m
    db2 = np.sum(dz2, axis=1, keepdims=True) / m
    dz1 = np.dot(w2, dz2) * d_sigmoid(A1)
    dw1 = np.dot(X, dz1.T) / m + lambd * w1 / m
    db1 = np.sum(dz1, axis=1, keepdims=True) / m
    # 更新权重
    w2 = w2 - alpha * dw2
    b2 = b2 - alpha * db2
    w1 = w1 - alpha * dw1
    b1 = b1 - alpha * db1
    if i % 10 == 0:
        print("train:" + str(i + 1) + " cost:" + str(-1 / m * np.sum(y * np.log(A2) + (1 - y) * np.log(1 - A2))))
else:
    print("train:" + str(i + 1) + " cost:" + str(-1 / m * np.sum(y * np.log(A2) + (1 - y) * np.log(1 - A2))))
print("w1:" + str(w1) + "\nw2:" + str(w1))
print("b1:" + str(b1) + "\nb2:" + str(b2))


def predict(x):  # 预测函数
    x = np.array([x])
    x = (x.T - np.mean(x)) / np.linalg.norm(x, ord=2, axis=1, keepdims=True)
    z1_test = np.dot(w1.T, x) + b1
    a1_test = sigmoid(z1_test)
    z2_test = np.dot(w2.T, a1_test) + b2
    a2_test = sigmoid(z2_test)
    return a2_test


print("predict 0 rate:%f%%" % ((1 - predict([0.1, 0.7, 0.5])) * 100))
print("predict 0 rate:%f%%" % ((1 - predict([0.9, 1.8, 0.5])) * 100))
print("predict 1 rate:%f%%" % (predict([1.2, 1.0, 1.5]) * 100))
print("predict 1 rate:%f%%" % (predict([1.8, 0.1, 1.9]) * 100))
