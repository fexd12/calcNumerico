import math

def fx(x):
    return (6*x-5)**(1/2)

def d2fx(x):
    return 9/(6*x-5)**(3/2)

def area(a,b):
    return (fx(a) + fx(b))*(b-a)*0.5

def erro(a,b, n):
    return ((b-a)**3) * max(a, b, 0.01) * (1/(12*(n**2)))

n = 100 
ini = 1.0
fim = 9.0
wdiv = (fim - ini)/ n 
print('tamanho do passo {}'.format(wdiv))

a = ini 
b = ini + wdiv

resultado = 0
c = 0
while True:
    if(a >= fim):
        break
    resultado += area(a,b)
    a = b
    b += wdiv
    c += 1

print('A integral de f(x): {}'.format(resultado*-1))
e = math.fabs(erro(ini, fim, n))
print('O erro é de: {}'.format(e))