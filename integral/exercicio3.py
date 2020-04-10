import math

def fx(x):
    return math.e**x

def integral(x):
    return math.e**x

def area(a, b):
    return (fx(a) + fx(b))*(b-a)*0.5

def erro(a, b, n):
    return ((b-a)**3) * maximo(a, b, 0.01) * (1/(12*(n**2)))

def maximo(a, b, t):
    maior = 0
    temp = 0
    while True:
        if(a >= b):
            break
        temp = integral(a)
        if(temp > maior):
            maior = temp
        a += t
    return maior

n = 4
n1 = 400
ini = 0.0
fim = 0.4
n_div = 0.1
n_div1 = 0.001

a = ini
b = ini + n_div
resultado = 0

a2 = ini
b2 = ini + n_div1
resultado2 = 0

while True:
    if(a >= fim):
        break
    resultado += area(a, b)
    a = b
    b += n_div

    if(a2 >= fim):
        break
    resultado += area(a2, b2)
    a2 = b2
    b2 += n_div1

print('Para divisoes com tamanho h = 0.1')
print('A integral de f(x): {}'.format(resultado))
er = math.fabs(erro(ini, fim, n))
print('O erro é de: {}\n'.format(er))
print('Para divisoes com h = 0.001')
print('A integral de f(x): {}'.format(resultado))
er = math.fabs(erro(ini, fim, n1))
print('O erro é de: {}'.format(er))