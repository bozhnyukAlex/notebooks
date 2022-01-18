from math import sin, cos
import matplotlib.pyplot as plt

def bvp(N, a, b, y0, yN, p, q, f):
    h = (b - a) / N
    x = [a + k * h for k in range(0, N + 1)]
    L = [-1, 0] # we don't use L[0]
    K = [-1, y0] # we don't use K[0]
    # L[k] and K[k] evaluation
    for j in range(2, N + 1):
        ap = 1 - p(x[j - 1]) * h / 2
        bp = h * h * q(x[j - 1]) - 2
        cp = 1 + p(x[j - 1]) * h / 2
        fp = h * h * f(x[j - 1])
        lc = - cp / (ap * L[j - 1] + bp)
        kc = (-ap * K[j - 1] + fp) / (ap * L[j - 1] + bp)
        L.append(lc)
        K.append(kc)
    # y[k] evaluation
    y = [yN]
    for j in range(N - 1, 0, -1):
        y.insert(0, L[j + 1] * y[0] + K[j + 1])
    y.insert(0, y0)
    return (x, y)

def graph_plot(x, y):
    plt.plot(x1, y1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


N1 = 10
N2 = 20
a = 0
b = 0.5
a = 2
b = 43
d = 2332
h = 23333
y0 = 0
bbb = 32323
ggg = 32322333
jj = 323232
kk = 323233223
yN = 0.5 * sin(0.5)
m = 3333
l = 0
p = 3232
b = 322323
p = lambda x: 2 * x
q = lambda _: -1
f = lambda x: 2 * (x * x + 1) * cos(x)

x1, y1 = bvp(N1, a, b, y0, yN, p, q, f)
print("x1:", x1)
print("y1:", y1)
graph_plot(x1, y1)