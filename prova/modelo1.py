import csv
import os
import matplotlib.pyplot

dados_confirmed = 'dados/confirmed_global.csv'
dados_deaths= 'dados/deaths_global.csv'
dados_recovered= 'dados/recovered_global.csv'

def delta(x):
    return int(x[len(x)-2]) - int(x[len(x)-1])

def abrirArquivo(path):
    with open(path,'r') as confirmed:
        leitor=csv.DictReader(confirmed,delimiter=',')
        for coluna in leitor:
            if coluna['Country/Region'] == 'Brazil':
                coluna3 = coluna.values()
    x=[]
    for e in coluna3:
        x.append(e)
    return x


def kUm1(x1, x4):
    return k11 * x4 - (k31+k21)*x1

def kDois1(x1,x4, k1):
    return k11 * (x4+k1/2) - (k31+k21)*(x1 + k1/2)

def kTres1(x1, x4, k2):
    return k11 * (x4+k2/2) - (k31+k21)*(x1 + k2/2)

def kQuatro1(x1, x4, k3):
    return k11 * (x4+k3) - (k31+k21)*(x1 + k3)


def kUm2(x1):
    return k31 * x1

def kDois2(x1, k1):
    return k31 * (x1+k1/2)

def kTres2(x1, k2):
    return k31 * (x1+k2/2)

def kQuatro2(x1, k3):
    return k31 * (x1+k3)


def kUm3(x1):
    return k21 * x1

def kDois3(x3, k1):
    return k21 * (x1+k1/2)

def kTres3(x3, k2):
    return k21 * (x1+k2/2)

def kQuatro3(x3, k3):
    return k21 * (x1+k3)


def kUm4(x4):
    return - k11 * x4

def kDois4(x4, k1):
    return - k11 * (x4+k1/2)

def kTres4(x4, k2):
    return - k11 * (x4+k2/2)

def kQuatro4(x4, k3):
    return - k11 * (x4+k3)


brasil_confirmed = abrirArquivo(dados_confirmed)
brasil_deaths = abrirArquivo(dados_deaths)
brasil_recovered = abrirArquivo(dados_recovered)

k11 = delta(brasil_confirmed)
k31 = delta(brasil_deaths) /k11
k21 = delta(brasil_recovered) /k11

casos = 209000000 * 0.7 - int(brasil_confirmed[len(brasil_confirmed)-1])

h = 1
t = 0

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

x1 =casos
x2 = int(brasil_confirmed[len(brasil_confirmed)-1])
x3 = int(brasil_deaths[len(brasil_deaths)-1])
x4 = int(brasil_recovered[len(brasil_recovered)-1])

auxX1 = 0
auxX2 = 0
auxX3 = 0
auxX4 = 0
erro = 0

matplotlib.pyplot.ioff()
graphT = []
graphX2 = []
graphX3 = []
graphX4 = []

while t < 800:
    auxX1 = x1
    auxX2 = x2
    auxX3 = x3
    auxX4 = x4

    rk11 = h*kUm1(x1,x4)
    rk21 = h*kUm2(x1)
    rk31 = h*kUm3(x1)
    rk41 = h*kUm4(x4)

    rk12 = h*kDois1(x1,x4, rk11)
    rk22 = h*kDois2(x1, rk21)
    rk32 = h*kDois3(x3, rk31)
    rk42 = h*kDois4(x4, rk41)

    rk13 = h*kTres1(x1,x4, rk12)
    rk23 = h*kTres2(x1, rk22)
    rk33 = h*kTres3(x3, rk32)
    rk43 = h*kTres4(x4, rk42)

    rk14 = h*kQuatro1(x1,x4, rk13)
    rk24 = h*kQuatro2(x1, rk23)
    rk34 = h*kQuatro3(x3, rk33)
    rk44 = h*kQuatro4(x4, rk43)

    print(f't:{t} || PP:{x1} || C:{x2} || M:{x3} || R:{x4}')

    graphT.append(t)
    graphX2.append(x2)
    graphX3.append(x3)
    graphX4.append(x4)

    x1 = x1 + (rk11 + 2 * rk12 + 2 * rk13 + rk14)/6
    x2 = x2 + (rk21 + 2 * rk22 + 2 * rk23 + rk24)/6
    x3 = x3 + (rk31 + 2 * rk32 + 2 * rk33 + rk34)/6
    x4 = x4 + (rk41 + 2 * rk42 + 2 * rk43 + rk44)/6
    erro = (x1 - auxX1) / auxX1 + (x2 - auxX2) / auxX2 + (x3 - auxX3) / auxX3 + (x4 - auxX4) / auxX4
    t = t + h

matplotlib.pyplot.plot(graphT,graphX2,label='C(t)')
matplotlib.pyplot.plot(graphT,graphX3,label='M(t)')
matplotlib.pyplot.plot(graphT,graphX4,label='R(t)')
matplotlib.pyplot.xlabel('tempo (t)')
matplotlib.pyplot.ylabel('valores (C(t) e M(t) e R(t))')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
