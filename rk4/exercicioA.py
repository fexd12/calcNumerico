import math as Math
import matplotlib.pyplot as plt










def fx1(x1,x2):
    return 0.02 * x2  - 0.03*x1

def fx2(x2,x1):
    return 0.03 *x1 - (0.02 + 0.01)*x2

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
auxa = 0 
auxc = 0 
erro =500

plt.ioff()

at=[]
ax1=[]
ax2=[]
while erro > 4e-5:

    auxa = x2
    auxc = x1
    k11 = h*fx1(x1,x2)
    k21 = h*fx2(x2,x1)
    
    k12 = h*fx1(t + h/2, x2 + k11/2)
    k22 = h*fx2(t + h/2, x1 + k21/2)

    k13 = h*fx1(t + h/2, x2 + k12/2)
    k23 = h*fx2(t + h/2, x1 + k22/2)

    k14 = h*fx1(t + h, x2 + k13)
    k24 = h*fx2(t + h, x1 + k23)

    print('t:{} || x1:{} || x2:{} || erro:{}'.format(t,x1,x2,erro))
    at.append(t)
    ax2.append(x2)
    ax1.append(x1)
    x1 = x1 + (k11 + 2 * k12 + 2 * k13 + k14) / 6
    x2 = x2 + (k21 + 2 * k22 + 2 * k23 + k24) / 6
    erro = (x2 - auxa) / auxa + (x1 - auxc) / auxc
    t = t + h

plt.plot(at,ax1,label='x1')
plt.plot(at,ax2,label='x2')
plt.xlabel('tempo (t)')
plt.ylabel('valores (x1 e x2)')
plt.title('rk4 graph')
plt.legend()
plt.show()