import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import lab3 as grad
from scipy.misc import derivative

import main as derivate
import  main as lab
import  DichotomyMethod

xf = lambda t: -(t ** 3 + 5 * t - 6) / 6
yf = lambda t: t
h = 0.1
eps = 0.01
count = 0
dx = 0.01
a, b = -1, 1
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

W0 = lambda t: (t-1)**2/2
W1 = lambda t: (t - 0) * (t - 2)
W2 = lambda t: (t - 0)  * (t - 2)  * t ** 2
W3 = lambda t: (t - 0)  * (t - 2) * math.cos(t)
W4 = lambda t: (t - 0) * (t - 2)  * t

W0y = lambda t: t
W1y = lambda t: (t - 1) * (t +1)
W2y = lambda t: (t - 1)  * (t + 1)  * t ** 2
W3y = lambda t: (t - 1)  * (t +1) * math.sin(t)
W4y = lambda t: (t - 1) * (t + 1)  * t





def asd(b1, b2, b3, b4):

    X1 = lambda t: W0(t) + b1 * W1(t) + b2 * W2(t)
    Y1 = lambda t: W0y(t) + b3 * W1y(t) + b4 * W2y(t)
    J1 = lambda t: 2*X1(t)*t - derivative(X1, t, 0.01)**2+(derivative(Y1, t, 0.01)**3/3)
    return trap(J1, -1, 1)

def main():
    derivate.main()
    exit()



def asd2(b1, b2, b3):
    X1 = lambda t: W0(t) + b1 * W1(t) + b2 * W2(t) + b3 * W3(t)
    Y1 = lambda t: W0y(t) + b1 * W1y(t) + b2 * W2y(t) + b3 * W3y(t)
    J1 = lambda t: X1(t) ** 2 + 2 * derivative(X1, t, 0.01) ** 2 + derivative(X1, t, 0.01, 2) ** 2
    return trap(J1, 0, 1)


def asd3(b1, b2, b3, b4):
    X1 = lambda t: W0(t) + b1 * W1(t) + b2 * W2(t) + b3 * W3(t) + b4 * W4(t)
    Y1 = lambda t: W0y(t) + b1 * W1y(t) + b2 * W2y(t) + b3 * W3y(t) + b4 * W4y(t)
    J1 = lambda t: X1(t) ** 2 + 2 * derivative(X1, t, 0.01) ** 2 + derivative(X1, t, 0.01, 2) ** 2
    return trap(J1, 0, 1)
if __name__ == '__main__':
    main()
    exit()


b1, b2 ,k1,k2= grad.naisk_spysk4(asd, -1, 0, -2 , 1,  0.1)  # -0.19533407856192705, 0.0204385904076095
X1 = lambda t: W0(t) + b1 * W1(t) + b2 * W2(t)
Y1 = lambda t:  W0y(t) + k1 * W1y(t) + k2 * W2y(t)
print(b1, b2, sep=', ')
print(k1, k2, sep=', ')

Graf(X1, "r")
Graf(Y1, "r")

b1, b2,b3 ,k1,k2, k3 = grad.naisk_spysk6(asd, -1, 0, -2 , 1,  0.1)  # -0.19533407856192705, 0.0204385904076095
X1 = lambda t: W0(t) + b1 * W1(t) + b2 * W2(t) + b3 * W3(t)
Y1 = lambda t:  W0y(t) + k1 * W1y(t) + k2 * W2y(t)
print(b1, b2,b3 ,sep=', ')
print(k1,k2, k3 ,sep=', ')

Graf(X1, "r")
Graf(Y1, "r")

b1, b2 , b3,b4 ,k1,k2,k3,k4= grad.naisk_spysk8(asd, -1, 0, -2 , 1,  0.1)  # -0.19533407856192705, 0.0204385904076095
X1 = lambda t: W0(t) + b1 * W1(t) + b2 * W2(t) + b3 * W3(t) + b4 * W4(t)
Y1 = lambda t:  W0y(t) + k1 * W1y(t) + k2 * W2y(t)
print(b1,b2,b3,b4, sep=', ')
print(k1,k2,k3,k4, sep=', ')

Graf(X1, "r")
Graf(Y1, "r")




Graf(yf)
Graf(xf)
plt.show()
