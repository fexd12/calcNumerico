import math as Math
import matplotlib.pyplot as plt

def fx1(x1,x2,x3):
    return 0.08 * x3 + 0.02* x2 - 0.03 * x1

def fx2(x2,x1):
    return 0.03 *x1 - (0.02 + 0.01)*x2

def fx3(t,x3):
    return -0.08 * x3

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
x1 = 100 
x2 = 10
x3 = 20
auxa = 0 
auxc = 0
auxd = 0
erro =0

plt.ioff()

at=[]
ax1=[]
ax2=[]
ax3 =[]

while t<18:

    auxa = x2
    auxc = x1
    auxd = x3

    k11 = h*fx1(x1,x2,x3)
    k21 = h*fx2(x1,x2)
    k31 = h*fx3(t,x3)
    
    k12 = h*fx1(t + h/2, x2 + k11/2,x3)
    k22 = h*fx2(t + h/2, x1 + k21/2)
    k32 = h*fx3(t + h/2, x1 + k31/2)

    k13 = h*fx1(t + h/2, x2 + k12/2,x3)
    k23 = h*fx2(t + h/2, x1 + k22/2)
    k33 = h*fx3(t + h/2, x1 + k32/2)


    k14 = h*fx1(t + h, x2 + k13,x3)
    k24 = h*fx2(t + h, x1 + k23)
    k34 = h*fx3(t + h, x1 + k33)

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