import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import math
import methods as met

dx = 0.001

grad_fx1 = lambda func, x0, x1: (func(x0 + dx, x1) - func(x0, x1)) / dx
grad_fx2 = lambda func, x0, x1: (func(x0, x1 + dx) - func(x0, x1)) / dx

grad2_fx1 = lambda func, x0, x1, x2: (func(x0+dx, x1, x2) - func(x0, x1, x2)) / dx
grad2_fx2 = lambda func, x0, x1, x2: (func(x0, x1 + dx, x2) - func(x0, x1, x2)) / dx
grad2_fx3 = lambda func, x0, x1, x2: (func(x0, x1, x2 + dx) - func(x0, x1, x2)) / dx

grad3_fx1 = lambda func, x0, x1, x2, x3: (func(x0+dx, x1, x2, x3) - func(x0, x1, x2, x3)) / dx
grad3_fx2 = lambda func, x0, x1, x2, x3: (func(x0, x1 + dx, x2, x3) - func(x0, x1, x2, x3)) / dx
grad3_fx3 = lambda func, x0, x1, x2, x3: (func(x0, x1, x2 + dx, x3) - func(x0, x1, x2, x3)) / dx
grad3_fx4 = lambda func, x0, x1, x2, x3: (func(x0, x1, x2 + dx, x3 + dx) - func(x0, x1, x2, x3)) / dx

def start(f_main):
    xf = (-20, 30)
    yf = (-30, 20)
    x_list = np.linspace(xf[0], xf[1], 50)
    y_list = np.linspace(yf[0], yf[1], 50)
    X, Y = np.meshgrid(x_list, y_list)
    Z = f_main(X, Y)
    fig, ax = plt.subplots(1, 1)
    cp = ax.contourf(X, Y, Z, levels=60)
    # ax.scatter(af, bf, c='y', s=5)
    fig.colorbar(cp)
    print("Исходный график:")
    return fig, ax


# рисование линий
def draw_lines(points, ax, col='r'):
    X = list()
    Y = list()
    for point in points:
        X.append(point[0])
        Y.append(point[1])
    ax.plot(X, Y, color=col)



def naisk_spysk(f_main, a, b, eps):

    # МЕТОД НАИСКОРЕЙШЕГО СПУСКА
    # 1.начальная точка Х0
    X0 = np.array([a, b])
    Xk = X0

    # 2.частные производные
    grad1 = grad_fx1(f_main, X0[0], X0[1])
    grad2 = grad_fx2(f_main, X0[0], X0[1])

    # 3.первичное направление S0
    Sk = np.array([-grad1, -grad2])
    iter_h = lambda k: f_main(Xk[0] + k * Sk[0], Xk[1] + k * Sk[1])
    # 4.вычисление Х1
    # h = met.DichotomyMethod(iter_h, 0, 5, eps)
    Xk = X0 + eps * Sk
    points = [X0, Xk]
    iterations = 1

    while True:
        iterations += 1

        # 5.частные производные и антиградиент
        grad1 = grad_fx1(f_main, points[-1][0], points[-1][1])
        grad2 = grad_fx2(f_main, points[-1][0], points[-1][1])

        # 6.поиск направления Sk
        Sk = np.array([-grad1, -grad2])


        # Вычисление h
        h = met.DichotomyMethod(iter_h, 0, 5, eps)

        # 7.вычисление новой Хk
        Xk = Xk + h[0] * Sk
        points.append(Xk)

        # погрешность
        accuracy = math.sqrt(math.pow(grad1, 2) + math.pow(grad2, 2))

        if accuracy < eps:
            eps -= eps/2
            if eps < 0.01:
                break
        print(f"Итераций: {iterations}", " b = ",Sk, "k = [",  Sk[0]* 0.28, -Sk[1]*0.184, "]")


    #draw_lines(points, ax)
    # display(fig)
    # plt.show()
    return Xk

def naisk_spysk3(f_main, a, b, c, eps):
    # fig, ax = start(f_main)
    # МЕТОД НАИСКОРЕЙШЕГО СПУСКА
    # 1.начальная точка Х0
    X0 = np.array([a, b, c])
    Xk = X0

    # 2.частные производные
    grad1 = grad2_fx1(f_main, X0[0], X0[1], X0[2])
    grad2 = grad2_fx2(f_main, X0[0], X0[1], X0[2])
    grad3 = grad2_fx3(f_main, X0[0], X0[1], X0[2])

    # 3.первичное направление S0
    Sk = np.array([-grad1, -grad2, -grad3])
    iter_h = lambda k: f_main(Xk[0] + k * Sk[0], Xk[1] + k * Sk[1], Xk[2] + k * Sk[3])
    # 4.вычисление Х1
    # h = met.DichotomyMethod(iter_h, 0, 5, eps)
    Xk = X0 + eps * Sk
    points = [X0, Xk]
    iterations = 1

    while True:
        iterations += 1

        # 5.частные производные и антиградиент
        grad1 = grad2_fx1(f_main, points[-1][0], points[-1][1], points[-1][2])
        grad2 = grad2_fx2(f_main, points[-1][0], points[-1][1], points[-1][2])
        grad3 = grad2_fx3(f_main, points[-1][0], points[-1][1], points[-1][2])

        # 6.поиск направления Sk
        Sk = np.array([-grad1, -grad2, -grad3])


        # Вычисление h
        # h = met.DichotomyMethod(iter_h, 0, 5, eps)

        # 7.вычисление новой Хk
        h = 1
        Xk = Xk + eps*h * Sk
        while True:
            Xk = Xk + eps * h * Sk
            Xk2 = Xk + eps * (h+eps) * Sk
            if f_main(Xk[0], Xk[1], Xk[2]) < f_main(Xk2[0], Xk2[1], Xk2[2]):
                break
            else:
                h += 0.1 * eps
        points.append(Xk + eps * h * Sk)

        print(f"Итераций: {iterations}", "b = ", Sk, "k = [",  Sk[0]* 0.28, -Sk[1]*0.184, Sk[2]*0.28, "]")
        # погрешность
        accuracy = math.sqrt(math.pow(grad1, 2) + math.pow(grad2, 2) + math.pow(grad3, 2))
        if accuracy < eps:
            eps -= eps/2
            if eps < 0.01:
                break

    print(f"Итераций: {iterations}")
    # draw_lines(points, ax)
    # display(fig)
    # plt.show()
    return Xk

def naisk_spysk4(f_main, a, b, c, d, eps):
    # fig, ax = start(f_main)
    # МЕТОД НАИСКОРЕЙШЕГО СПУСКА
    # 1.начальная точка Х0
    X0 = np.array([a, b, c, d])
    Xk = X0

    # 2.частные производные
    grad1 = grad3_fx1(f_main, X0[0], X0[1], X0[2], X0[3])
    grad2 = grad3_fx2(f_main, X0[0], X0[1], X0[2], X0[3])
    grad3 = grad3_fx3(f_main, X0[0], X0[1], X0[2], X0[3])
    grad4 = grad3_fx3(f_main, X0[0], X0[1], X0[2], X0[3])

    # 3.первичное направление S0
    Sk = np.array([-grad1, -grad2, -grad3, -grad4])
    # iter_h = lambda k: f_main(Xk[0] + k * Sk[0], Xk[1] + k * Sk[1], Xk[2] + k * Sk[3])
    # 4.вычисление Х1
    # h = met.DichotomyMethod(iter_h, 0, 5, eps)
    Xk = X0 + eps * Sk
    points = [X0, Xk]
    iterations = 1

    while True:
        iterations += 1

        # 5.частные производные и антиградиент
        grad1 = grad3_fx1(f_main, points[-1][0], points[-1][1], points[-1][2], points[-1][3])
        grad2 = grad3_fx2(f_main, points[-1][0], points[-1][1], points[-1][2], points[-1][3])
        grad3 = grad3_fx3(f_main, points[-1][0], points[-1][1], points[-1][2], points[-1][3])
        grad4 = grad3_fx4(f_main, points[-1][0], points[-1][1], points[-1][2], points[-1][3])

        # 6.поиск направления Sk
        Sk = np.array([-grad1, -grad2, -grad3, -grad4])


        # Вычисление h
        # h = met.DichotomyMethod(iter_h, 0, 5, eps)

        # 7.вычисление новой Хk
        h = 1
        Xk = Xk + eps * h * Sk
        while True:
            Xk = Xk + eps * h * Sk
            Xk2 = Xk + eps * (h + eps) * Sk
            if f_main(Xk[0], Xk[1], Xk[2], Xk[3]) < f_main(Xk2[0], Xk2[1], Xk2[2], Xk2[3]):
                break
            else:
                h += 0.1 * eps
        points.append(Xk + eps * h * Sk)

        print(f"Итераций: {iterations}", "b = ", Sk, "k = [",  Sk[0]* 0.28, -Sk[1]*0.184, Sk[2]*0.28, Sk[3]*0.22, "]")
        # погрешность
        accuracy = math.sqrt(math.pow(grad1, 2) + math.pow(grad2, 2) + math.pow(grad3, 2)+ math.pow(grad4, 2))
        if accuracy < eps:
            eps -= eps/2
            if eps < 0.01:
                break

    # print(f"Итераций: {iterations}")
    # draw_lines(points, ax)
    # display(fig)
    # plt.show()
    return Xk

