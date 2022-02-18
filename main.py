import math
import numpy as np
import matplotlib.pyplot as plt
import lab3 as grad
import  DichotomyMethod as graphic
from scipy.misc import derivative
# NEW DEVELOP CHANGE
y = lambda t: (1 - t) * sh(t)
h = 0.1
eps = 0.01
count = 0
dx = 0.01
a, b = 0, 1
dt = 0.001
t = int(1 / dt)


def trap(func, a, b, h=0.001):
    s = 0.5 * (func(a) + func(b))
    x = a + h
    while (x <= b - h):
        s += func(x)
        x += h
    return h * s


def Graf(f, col='y'):
    x1 = np.linspace(a, b, t)
    x2 = np.linspace(a, b, t)
    for i in range(t):
        x2[i] = f(x1[i])
    plt.plot(x1, x2, color=col)


sh = lambda x: (math.exp(x) - math.exp(-x)) / 2
ch = lambda x: (math.exp(x) + math.exp(-x)) / 2

a1 = 1 - sh(1)
a2 = sh(1) - 2
a3 = 1
a4 = 0

W0 = lambda t: a1 * t ** 3 + a2 * t ** 2 + a3 * t + a4
W1 = lambda t: (t - 0) ** 2 * (t - 1) ** 2
W2 = lambda t: (t - 0) ** 2 * (t - 1) ** 2 * t ** 2
W3 = lambda t: (t - 0) ** 2 * (t - 1) ** 2 * math.cos(t)
W4 = lambda t: (t - 0) ** 2 * (t - 1) ** 2 * t


# x = 1
# print(X1(x))
# print(derivative(X1, x, 0.001))


def asd(b1, b2):
    X1 = lambda t: W0(t) + b1 * W1(t) + b2 * W2(t)
    J1 = lambda t: X1(t) ** 2 + 2 * derivative(X1, t, 0.01) ** 2 + derivative(X1, t, 0.01, 2) ** 2
    return trap(J1, 0, 1)



def asd2(b1, b2, b3):
    X1 = lambda t: W0(t) + b1 * W1(t) + b2 * W2(t) + b3 * W3(t)
    J1 = lambda t: X1(t) ** 2 + 2 * derivative(X1, t, 0.01) ** 2 + derivative(X1, t, 0.01, 2) ** 2
    return trap(J1, 0, 1)


def asd3(b1, b2, b3, b4):
    X1 = lambda t: W0(t) + b1 * W1(t) + b2 * W2(t) + b3 * W3(t) + b4 * W4(t)
    J1 = lambda t: X1(t) ** 2 + 2 * derivative(X1, t, 0.01) ** 2 + derivative(X1, t, 0.01, 2) ** 2
    return trap(J1, 0, 1)
def main():

    b1, b2 = grad.naisk_spysk(asd, 1, 2, 0.1)  # -0.19533407856192705, 0.0204385904076095



    b1, b2, b3 = grad.naisk_spysk3(asd2, -1, 0, 1, 0.1)




    b1, b2, b3, b4 = grad.naisk_spysk4(asd3, -1, 0, 1, 0, 0.1)

    graphic.main()







