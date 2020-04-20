import math as Math
import matplotlib.pyplot as plt


def kUm1(x1, x2, x3):
    return 0.08 * x3 + 0.02* x2 - 0.03 * x1

def kDois1(x1, x2, x3, k1):
    return 0.08 * (x3 + k1/2) + 0.02*( x2 + k1/2) - 0.03 * (x1 + k1/2)

def kTres1(x1, x2, x3, k2):
    return 0.08 * (x3 + k2/2) + 0.02*( x2 + k2/2) - 0.03 * (x1 + k2/2)

def kQuatro1(x1, x2, x3, k3):
    return 0.08 * (x3 + k3) + 0.02*( x2 + k3) - 0.03 * (x1 + k3)


def kUm2(x1, x2):
    return 0.03 * x1 - (0.01 + 0.02) * x2

def kDois2(x1, x2, k1):
    return 0.03 * (x1 + k1 / 2) - (0.01 + 0.02) * (x2 + k1 / 2)

def kTres2(x1, x2, k2):
    return 0.03 * (x1 + k2 / 2) - (0.01 + 0.02) * (x2 + k2 / 2)

def kQuatro2(x1, x2, k3):
    return 0.03 * (x1 + k3) - (0.01 + 0.02) * (x2 + k3)


def kUm3(x3):
    return -0.08 * x3

def kDois3(x3, k1):
    return -0.08 * (x3 + k1 / 2)

def kTres3(x3, k2):
    return -0.08 * (x3 + k2 / 2)

def kQuatro3(x3, k3):
    return -0.08 * (x3 + k3)


h = 0.001
t = 0.1
k11 = 0
k12 = 0
k13 = 0
k14 = 0
k21 = 0
k22 = 0 
k23 = 0
k24 = 0
k31 =0
k32 =0
k33 =0
k34 =0
x1 = 100 
x2 = 10
x3 = 20
auxa = 0 
auxc = 0
auxd = 0
erro =500

plt.ioff()

at=[]
ax1=[]
ax2=[]
ax3 =[]

while t<800:

    auxa = x2
    auxc = x1
    auxd = x3

    k11 = h*kUm1(x1, x2,x3)
    k21 = h*kUm2(x1, x2)

    k12 = h*kDois1(x1, x2,x3, k11)
    k22 = h*kDois2(x1, x2, k21)

    k13 = h*kTres1(x1, x2,x3, k12)
    k23 = h*kTres2(x1, x2, k22)

    k14 = h*kQuatro1(x1, x2,x3, k13)
    k24 = h*kQuatro2(x1, x2, k23)

    k31 = h*kUm3(x3)
    k32 = h*kDois3(x3,k31)
    k33 = h*kTres3(x3,k32)
    k34 = h*kQuatro3(x3,k33)

    print('t:{} || x1:{} || x2:{} || x3:{} || erro:{}'.format(t,x1,x2,x3,erro))

    at.append(t)
    ax2.append(x2)
    ax1.append(x1)
    ax3.append(x3)
    x1 = x1 + (k11 + 2 * k12 + 2 * k13 + k14) / 6
    x2 = x2 + (k21 + 2 * k22 + 2 * k23 + k24) / 6
    x3 = x3 + (k31 + 2 * k32 + 2 * k33 + k34) / 6
    erro = (x2 - auxa) / auxa + (x1 - auxc) / auxc + (x3 - auxd) / auxd
    t = t + h

plt.plot(at,ax1,label='x1')
plt.plot(at,ax2,label='x2')
plt.plot(at,ax3,label='x3')
plt.xlabel('tempo (t)')
plt.ylabel('valores (x1,x2 e x3)')
plt.title('rk4 graph')
plt.legend()
plt.show()