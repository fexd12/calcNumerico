import math
import matplotlib.pyplot as plt

def alphaN(vm):
    return (0.01 * (vm - 10)) / (math.exp((vm - 10) / 10) - 1)

def alphaM(vm):
    return (0.1 * (vm  - 25)) / (math.exp((vm - 25) / 10) - 1)

def alphaH(vm):
    return 0.07 * (math.exp(vm / 20))


def betaN(vm):
    return 0.125 * (math.e**(vm / 80))

def betaM(vm):
    return 4 * (math.e**(vm / 18))

def betaH(vm):
    return (1 / (math.e**((vm + 30) / 10) + 1))


def dndt (n,vm,T = 0.01*10**(-3)):
    return n+T * (alphaN(vm) * (1-n)-betaN(vm)*n)

def dmdt (m,vm,T = 0.01*10**(-3)):
    return m+T * (alphaM(vm) * (1-m)-betaM(vm)*m)

def dhdt (h,vm, T = 0.01*10**(-3)):
    return h+T * (alphaH(vm) * (1-h)-betaH(vm)*h) 

gK = 3.60 
vK = -77*10**(-3)

gNa = 12
vNa = 50*10**(-3)

gL = 0.030
vL = -54.402*10**(-3)

v0 = -65.002*10**(-3)
t0 = 0 

n0 = 0.3176
m0 = 0.0529
h0 = 0.5961

auxN = n0
auxM = m0
auxH = h0


Tf = 0.01*10**(-3)
Cm = 1*10**(-6)
x = Tf/Cm

tensao= [] 
tempo= []
tempo.append(t0)
tensao.append(v0)

pN= gK*(n0**4)*(tensao[0]-vK)
pM= gNa*(m0**3)*(tensao[0]-vNa)
pL= gL*(tensao[0] - vL)

auxP = tensao[0]-(pN+pM+pL)*x
tensao.append(auxP)
tempo.append(t0 + Tf)

N = [n0]
N.append(n0)

M = [m0]
M.append(m0)

H =[h0]
H.append(h0)

f = 1 
n = 0
stop = 0.25*10**(-3)
while n < stop:
    auxT = f
    auxN = dndt (auxN, tensao[f])
    N.append(auxN)
    auxM = dmdt (auxM, tensao[f])
    M.append(auxN)
    auxH = dhdt (auxH, tensao[f])
    H.append(auxH)
    
    pN= gK*(n0**4)*(tensao[f]-vK)
    pM= gNa*(m0**3)*auxH*(tensao[f]-vNa)
    pL= gL*(tensao[f]-vL)

    auxP1 = tensao[auxT] - (pN+pM+pL) * x
    tensao.append(auxP1)
    
    f += 1
    n += Tf
    tempo.append(n)
plt.plot(tempo,tensao)
plt.xlabel('tempo (t)')
plt.ylabel('valores v(t)')
plt.legend()
plt.show()