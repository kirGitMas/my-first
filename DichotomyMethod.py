import numpy as np
import matplotlib.pyplot as plt
import math as mth

CoefficientCX = [0, 2, 2, 2, 2]
CoefficientCY = [0, 2, -1, 8, -1]
FirstX = 2
SecondX = 0
FirstY = -1
SecondY = 1
FirstT = -1
SecondT = 1

E = 0.01  # РўРѕС‡РЅРѕСЃС‚СЊ СЃСЂР°РІРЅРµРЅРёСЏ РёРЅС‚РµРіСЂР°Р»РѕРІ
H = 0.005  # РўРѕС‡РЅРѕСЃС‚СЊ РёРЅС‚РµРіСЂР°Р»Р°
N = 2  # Р§РёСЃР»Рѕ РєРѕСЌС„С„РёС†РёРµРЅС‚РѕРІ

INTEGRAL = -0.31


# РќР°С‡Р°Р»СЊРЅС‹Рµ С„СѓРЅРєС†РёРё


def functionX(t):
    return -(t ** 3 + 5 * t - 6) / 6


def functionY(t):
    return t


# Р¤СѓРЅРєС†РёСЏ РёРЅС‚РµРіСЂРёСЂРѕРІР°РЅРёСЏ


def functionIntegrand(CX, CY, t):
    return 2 * t * functionXWN(CX, t) - (functionXWNShtrix(CX, t) ** 2) + (functionYWNShtrix(CY, t) ** 3) / 3


# Р¤СѓРЅРєС†РёРё РїРѕ X


def functionXW0(t):
    return 1 - t


def functionXW0Shtrix():
    return -1


def functionXWN(C, t):
    if N == 2:
        return functionXW2(C, t)
    if N == 3:
        return functionXW3(C, t)
    if N == 4:
        return functionXW4(C, t)


def functionXWNShtrix(C, t):
    if N == 2:
        return functionXW2Shtrix(C, t)
    if N == 3:
        return functionXW3Shtrix(C, t)
    if N == 4:
        return functionXW4Shtrix(C, t)


def functionXW2(C, t):
    return C[1] * t * (t + 1) * (t - 1) + C[2] * (t ** 2) * (t + 1) * (t - 1) + functionXW0(t)


def functionXW2Shtrix(C, t):
    return C[1] * (1 * (t ** (1 - 1)) * ((t ** 2) - 1) + (t ** 1) * 2 * t) + C[2] * (
                2 * (t ** (2 - 1)) * ((t ** 2) - 1) + (t ** 2) * 2 * t) + functionXW0Shtrix()


def functionXW3(C, t):
    return (C[1] * t * (t + 1) * (t - 1)) + (C[2] * (t ** 2) * (t + 1) * (t - 1)) + (
            C[3] * (t ** 3) * (t + 1) * (t - 1)) + functionXW0(t)


def functionXW3Shtrix(C, t):
    return C[1] * (1 * (t ** (1 - 1)) * ((t ** 2) - 1) + (t ** 1) * 2 * t) + C[2] * (
                2 * (t ** (2 - 1)) * ((t ** 2) - 1) + (t ** 2) * 2 * t) + C[3] * (
                       3 * (t ** (3 - 1)) * ((t ** 2) - 1) + (t ** 3) * 2 * t) + functionXW0Shtrix()


def functionXW4(C, t):
    return (C[1] * t * (t + 1) * (t - 1)) + (C[2] * (t ** 2) * (t + 1) * (t - 1)) + (
            C[3] * (t ** 3) * (t + 1) * (t - 1)) + (C[4] * (t ** 4) * (t + 1) * (t - 1)) + functionXW0(t)


def functionXW4Shtrix(C, t):
    return C[1] * (1 * (t ** (1 - 1)) * ((t ** 2) - 1) + (t ** 1) * 2 * t) + C[2] * (
                2 * (t ** (2 - 1)) * ((t ** 2) - 1) + (t ** 2) * 2 * t) + C[3] * (
                       3 * (t ** (3 - 1)) * ((t ** 2) - 1) + (t ** 3) * 2 * t) + C[4] * (
                       4 * (t ** (4 - 1)) * ((t ** 2) - 1) + (t ** 4) * 2 * t) + functionXW0Shtrix()


# Р¤СѓРЅРєС†РёРё РїРѕ Y
def functionYW0(t):
    return t


def functionYW0Shtrix():
    return 1


def functionYWN(C, t):
    if N == 2:
        return functionYW2(C, t)
    if N == 3:
        return functionYW3(C, t)
    if N == 4:
        return functionYW4(C, t)


def functionYWNShtrix(C, t):
    if N == 2:
        return functionYW2Shtrix(C, t)
    if N == 3:
        return functionYW3Shtrix(C, t)
    if N == 4:
        return functionYW4Shtrix(C, t)


def functionYW2(C, t):
    return C[1] * t * (t + 1) * (t - 1) + C[2] * (t ** 2) * (t + 1) * (t - 1) + functionYW0(t)


def functionYW2Shtrix(C, t):
    return C[1] * (1 * (t ** (1 - 1)) * ((t ** 2) - 1) + (t ** 1) * 2 * t) + C[2] * (
                2 * (t ** (2 - 1)) * ((t ** 2) - 1) + (t ** 2) * 2 * t) + functionYW0Shtrix()


def functionYW3(C, t):
    return (C[1] * t * (t + 1) * (t - 1)) + (C[2] * (t ** 2) * (t + 1) * (t - 1)) + (
            C[3] * (t ** 3) * (t + 1) * (t - 1)) + functionYW0(t)


def functionYW3Shtrix(C, t):
    return C[1] * (1 * (t ** (1 - 1)) * ((t ** 2) - 1) + (t ** 1) * 2 * t) + C[2] * (
                2 * (t ** (2 - 1)) * ((t ** 2) - 1) + (t ** 2) * 2 * t) + C[3] * (
                       3 * (t ** (3 - 1)) * ((t ** 2) - 1) + (t ** 3) * 2 * t) + functionYW0Shtrix()


def functionYW4(C, t):
    return (C[1] * t * (t + 1) * (t - 1)) + (C[2] * (t ** 2) * (t + 1) * (t - 1)) + (
            C[3] * (t ** 3) * (t + 1) * (t - 1)) + (C[4] * (t ** 4) * (t + 1) * (t - 1)) + functionYW0(t)


def functionYW4Shtrix(C, t):
    return C[1] * (1 * (t ** (1 - 1)) * ((t ** 2) - 1) + (t ** 1) * 2 * t) + C[2] * (
                2 * (t ** (2 - 1)) * ((t ** 2) - 1) + (t ** 2) * 2 * t) + C[3] * (
                       3 * (t ** (3 - 1)) * ((t ** 2) - 1) + (t ** 3) * 2 * t) + C[4] * (
                       4 * (t ** (4 - 1)) * ((t ** 2) - 1) + (t ** 4) * 2 * t) + functionYW0Shtrix()


# РњРµС‚РѕРґС‹


def methodSimpsona(CX, CY):
    h = H
    a = FirstT
    n = (SecondT - FirstT) / h
    sumIntegral = 0.0
    for Iterations in range(int(n)):
        x = a + Iterations * h
        if (Iterations == 0) | (Iterations == n):
            sumIntegral = sumIntegral + functionIntegrand(CX, CY, x)
        elif Iterations % 2 == 0:
            sumIntegral = sumIntegral + (2 * functionIntegrand(CX, CY, x))
        else:
            sumIntegral = sumIntegral + (4 * functionIntegrand(CX, CY, x))
    return sumIntegral * h / 3


def methodRitz():
    CX = CoefficientCX
    CY = CoefficientCY
    integralSearch = methodSimpsona(CX, CY)
    while mth.fabs(INTEGRAL - integralSearch) > E:
        if INTEGRAL > integralSearch:
            Coef1 = CX[1] * 1.04
            Coef2 = CX[2] * 1.04
            Coef3 = CX[3] * 1.04
            Coef4 = CX[4] * 1.04
            CX = [0, Coef1, Coef2, Coef3, Coef4]
            Coef1 = CY[1] * 1.5
            Coef2 = CY[2] * 1.5
            Coef3 = CY[3] * 1.5
            Coef4 = CY[4] * 1.5
            CY = [0, Coef1, Coef2, Coef3, Coef4]
        else:
            Coef1 = CX[1] * 0.9
            Coef2 = CX[2] * 0.9
            Coef3 = CX[3] * 0.9
            Coef4 = CX[4] * 0.9
            CX = [0, Coef1, Coef2, Coef3, Coef4]
            Coef1 = CY[1] * 0.78
            Coef2 = CY[2] * 0.78
            Coef3 = CY[3] * 0.7
            Coef4 = CY[4] * 0.78
            CY = [0, Coef1, Coef2, Coef3, Coef4]
        integralSearch = methodSimpsona(CX, CY)
    return [CX, CY]


# Р“СЂР°С„РёРє
def functionPlotX(C, t):
    if N == 2:
        return functionXW2(C, t)
    if N == 3:
        return functionXW3(C, t)
    if N == 4:
        return functionXW4(C, t)


def functionPlotY(C, t):
    if N == 2:
        return functionYW2(C, t)
    if N == 3:
        return functionYW3(C, t)
    if N == 4:
        return functionYW4(C, t)


def plotCreator(C):
    tArray = np.linspace(FirstT, SecondT, 100)
    xArray = [functionX(Iterations) for Iterations in tArray]
    yArray = [functionY(Iterations) for Iterations in tArray]
    xResultArray = [functionPlotX(C[0], Iterations) for Iterations in tArray]
    yResultArray = [functionPlotY(C[0], Iterations) for Iterations in tArray]
    plt.plot(tArray, xArray, tArray, yArray, tArray, xResultArray, tArray, yResultArray)
    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('x')
    plt.legend(['True Func X', 'True Func Y', 'Method X', 'Method Y'])
    plt.show()


def main():
    list_out = methodRitz()
    print("Для X: ")
    for i in range(1, N + 1):
        print(" C[", i, "] = ", list_out[0][i])
    print("Для Y: ")
    for i in range(1, N + 1):
        print(" C[", i, "] = ", list_out[1][i])
    plotCreator(list_out)
