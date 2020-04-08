import math

def fx(x):
    return 1/((x**2)-1)

def d2fx(x):
    return -2*(-3**2 - 1)/(x**2 - 1)**3

def area(a, b):
    return (fx(a) + fx(b))*(b-a)*0.5

def max(a, b, inc):
    maior = -999
    temp = 0
    while True:
        if(a >= b):
            break
        temp = d2fx(a)
        if(temp > maior):
            maior = temp
        a = a + inc
    return maior

def erro(a, b, n):
    return ((b-a)**3) * max(a, b, 0.01) * (1/(12*(n**2)))

n = 8
n1 = 800
ini = 0.0
fim = 0.8
wdiv = 0.1
wdiv1 = 0.001
a = ini
b = ini + wdiv
resultado = 0
a2 = ini
b2 = ini + wdiv1
resultado2 = 0

while True:
    if(a >= fim):
        break
    resultado += area(a, b)
    a = b
    b += wdiv

    if(a2 >= fim):
        break
    resultado2 += area(a2, b2)
    a2 = b2
    b2 += wdiv1

print('Para divisoes com h = 0.1')
print('A integral de f(x): {}'.format(resultado))
e = math.fabs(erro(ini, fim, n))
print('O erro é de: {}\n'.format(e))
print('Para divisoes com tamanho h = 0.001')
print('A integral de f(x): {}'.format(resultado))
e = math.fabs(erro(ini, fim, n1))
print('O erro é de: {}'.format(e))