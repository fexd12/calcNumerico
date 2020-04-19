import math
import numpy as np

#instalar biblioteca numpy  - pip install numpy - para realizar os testes

#FELIPE AMORIM DE MELO - BEC

def Fx(v):
    teste = v + (((-0.2)*v**2)/1 - 9.81)*0.01
    return teste

Vini = float(input('digite a velocidade inicial: '))

N = 1000
x = np.empty(N)
n= 0

Vfinal = math.sqrt((1*9.81/0.2))

x[0] = Vini
n=1 
while n < N:
    if x[n-1] < 0.0:
        break
    
    if x[n-1] == Vfinal:
        print('igual vfinal')
    if x[n-1] > Vfinal:
        print('velocidade maior que vfinal ')
    if x[n-1] < Vfinal:
        print('velocidade menor que vfinal')
    x[n] = Fx(x[n-1])
    print('Tempo:{} || Velocidade:{}'.format(n,x[n]))
    n=n+1
