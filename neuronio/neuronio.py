import math
import matplotlib.pyplot as plt


def alphaN(vm):
    return (0.01 * (vm + 10)) / (math.e**((vm + 10) / 10) - 1)


def alphaM(vm):
    return (0.1 * (vm + 25)) / (math.e**((vm + 25) / 10) - 1)


def alphaH(vm):
    return 0.07 * (math.e**(vm / 20))


def betaN(vm):
    return 0.125 * (math.e**(vm / 80))


def betaM(vm):
    return 4 * (math.e**(vm / 18))


def betaH(vm):
    return (1 / (math.e**((vm + 30) / 10) + 1))


def densidadeCorrente(m, n, h, vm):
    return ((gna * math.pow(m, 3)*h * (vm - ena) + gk*math.pow(n, 4)*(vm-ek) + gl*(vm - ev)))


def kUm1(vm):  # n
    return alphaN(vm) * (1 - n) - betaN(vm) * n


def kDois1(vm, k1):
    return alphaN(vm) * (1 - n + k1/2) - betaN(vm ) * (n + k1/2)


def kTres1(vm, k2):
    return alphaN(vm ) * (1 - n + k2/2) - betaN(vm) * (n + k2/2)


def kQuatro1(vm, k3):
    return alphaN(vm ) * (1 - n + k3) - betaN(vm + k3) * (n + k3)


def kUm2(vm):  # m
    return alphaM(vm) * (1 - m) - betaM(vm) * m


def kDois2(vm, k1):
    return alphaM(vm ) * (1 - m + k1/2) - betaM(vm ) * (m + k1/2)


def kTres2(vm, k2):
    return alphaM(vm ) * (1 - m + k2/2) - betaM(vm ) * (m + k2/2)


def kQuatro2(vm, k3):
    return alphaM(vm ) * (1 - m + k3) - betaM(vm ) * (m + k3)


def kUm3(vm):  # h
    return alphaH(vm) * (1 - h) - betaH(vm) * h


def kDois3(vm, k1):
    return alphaH(vm ) * (1 - h + k1/2) - betaH(vm ) * (h + k1/2)


def kTres3(vm, k2):
    return alphaH(vm ) * (1 - h + k2/2) - betaH(vm ) * (h + k2/2)


def kQuatro3(vm, k3):
    return alphaH(vm ) * (1 - h + k3) - betaH(vm) * (h+ k3)


def kUm4(vm):  # i

    return densidadeCorrente(m, n, h, vm)


def kDois4(vm, k1):
    return densidadeCorrente(m+ k1 / 2, n+ k1 / 2, h+ k1 / 2, vm )


def kTres4(vm, k2):
    return densidadeCorrente(m+ k2 / 2, n+ k2 / 2, h+ k2 / 2, vm )


def kQuatro4(vm, k3):
    return densidadeCorrente(m+ k3, n+ k3, h+ k3, vm )


plt.ioff()

gk = 3.60
gna = 12.0
gl = 0.03

vm = -65.002 * math.pow(10, -3)
cm = 1 * math.pow(10, -6)

ek = -77 * math.pow(10, -3)
ev = -54 * math.pow(10, -3)
ena = 50 * math.pow(10, -3)
ist = 1 * math.pow(10, -6)

n = 0.3176
m = 0.0529
h = 0.5961
i = 0


rk11 = 0
rk12 = 0
rk13 = 0
rk14 = 0

rk21 = 0
rk22 = 0
rk23 = 0
rk24 = 0

rk31 = 0
rk32 = 0
rk33 = 0
rk34 = 0

rk41 = 0
rk42 = 0
rk43 = 0
rk44 = 0

graphT = []
graphN = []
graphM = []
graphH = []
graphI = []
graphVM = []

t = 0
g = 0.1

while t < 10:

    rk11 = g*kUm1(vm)
    rk21 = g*kUm2(vm)
    rk31 = g*kUm3(vm)
    rk41 = g*kUm4(vm)

    rk12 = g*kDois1(vm, rk11)
    rk22 = g*kDois2(vm, rk21)
    rk32 = g*kDois3(vm, rk31)
    rk42 = g*kDois4(vm, rk41)

    rk13 = g*kTres1(vm, rk12)
    rk23 = g*kTres2(vm, rk22)
    rk33 = g*kTres3(vm, rk32)
    rk43 = g*kTres4(vm, rk42)

    rk14 = g*kQuatro1(vm, rk13)
    rk24 = g*kQuatro2(vm, rk23)
    rk34 = g*kQuatro3(vm, rk33)
    rk44 = g*kQuatro4(vm, rk43)

    n = n + (rk11 + 2 * rk12 + 2 * rk13 + rk14)/6
    m = m + (rk21 + 2 * rk22 + 2 * rk23 + rk24)/6
    h = h + (rk31 + 2 * rk32 + 2 * rk33 + rk34)/6
    i = i + (rk41 + 2 * rk42 + 2 * rk43 + rk44)/6

    graphT.append(t)
    graphVM.append(vm)
    graphN.append(n)
    graphM.append(m)
    graphH.append(h)
    graphI.append(i)

    print(f't:{t} || M:{m} || N:{n} || H:{h}')

    t = t + g

# plt.plot(graphT, graphM, label='m(t)')
# plt.plot(graphT, graphH, label='h(t)')
plt.plot(graphT, graphN, label='n(t)')
plt.xlabel('tempo (t)')
plt.ylabel('valores m(t),h(t),n(t)')
plt.legend()
plt.show()