import math
import numpy as np

#instalar biblioteca numpy  - pip install numpy - para realizar os testes

#FELIPE AMORIM DE MELO - BEC
#usado fuzil M4A1
#velocide de disparo = 884 m/s
#calibre 5.56x45mm
# massa = 3,1 Kg

def radianos(x):
    return x * math.pi / 180

velocidadeInicial = 884
massa = 0.0031

area = 0.25 * math.pi * 0.00556
b = 0.5 * area * 1.25 * 0.5
g = 9.81
N=1000

angInicial = float(input('Digite o Angulo'))
ang = radianos(angInicial)

passo = 0.001

n = 0 
altura = 0
distancia = 0

x = np.empty(N)
y = np.empty(N)
dx = np.empty(N)
dy = np.empty(N)
energiaX = np.empty(N)
energiay = np.empty(N) 
vx = np.empty(N)
vy = np.empty(N)

vx[n] = velocidadeInicial * math.cos(ang)
vy[n] = velocidadeInicial * math.sin(ang)

energiaX[n] = massa *0.5 * vx[n] **2
energiay[n] = massa *0.5 * vy[n] **2

x[0] = vx[n] * passo
y[0] = vy[n] * passo

dx[0] = x[n] - distancia
dy[0] = y[n] - altura

altura = y[n]
distancia = x[n]

ang = math.atan((dy[n])/(dx[n]))
alturamax= 0

n=1

while n < N:
    if vy[n-1] < 0.0001:
        break
    if altura < 0.001:
        break

    energiaX[n] = energiaX[n-1] - b * vx[n-1]**2
    energiay[n] = energiay[n-1] - b * vy[n-1]**2

    if energiaX[n] < 0 and massa*0.5 + b* dx[n-1] > 0:
        break
    if energiaX[n] > 0 and (massa*0.5 + b* dx[n-1]) < 0:
        dx[n-1] = math.fabs(dx[n-1])
    
    vx[n]=(energiaX[n]/(massa*0.5 + b* dx[n-1]))**(1/2)

    if((energiay[n]) < 0 and (massa*0.5 + b* dy[n-1]) > 0):
        break
    if(energiay[n]) > 0 and (massa*0.5 + b* dy[n-1]) < 0:
        dy[n-1] = math.fabs(dy[n-1])
    
    vy[n] = ((energiay[n])/(massa*0.5 + b* dy[n-1]))**(1/2)

    x[n] = x[n-1] + vx[n-1] * passo
    y[n] = y[n-1] + vy[n-1] * passo

    distancia = x[n]
    altura = y[n]

    dx[n] = x[n] - x[n-1]
    dy[n] = y[n] - y[n-1]

    ang = math.atan(dy[n]/dx[n])

    print("Tempo: {:.2} s || Velocidade em X: {:.5} || Velocidade em Y: {:.5} || Altura: {:.5} || Distância: {:.5}".format(n*passo,vx[n],vy[n],altura,distancia))

    n = n + 1
alturaMax = np.amax(y)
print("Para um ângulo {}º || Alcance máximo: {:.5} m || Altura máxima: {:.5} m || Em {} s".format(angInicial,np.amax(x),alturaMax,n*passo))