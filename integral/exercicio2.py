import math

def fx(x):
    return 1/((x**2)-1)

def integral(x):
    
    return (math.log(math.fabs(x-1)) - math.log(math.fabs(x+1)) ) /2

def area(a, b):
    return (fx(a) + fx(b))*(b-a)*0.5

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

def erro(a, b, n):
    return ((b-a)**3) * maximo(a, b, 0.01) * (1/(12*(n**2)))

n = 8
n1 = 800
ini = 0.0
fim = 0.8
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
    resultado2 += area(a2, b2)
    a2 = b2
    b2 += n_div1

print('Para divisoes com h = 0.1')
print('A integral de f(x): {}'.format(resultado))
e = math.fabs(erro(ini, fim, n))
print('O erro é de: {}\n'.format(e))
print('Para divisoes com tamanho h = 0.001')
print('A integral de f(x): {}'.format(resultado))
e = math.fabs(erro(ini, fim, n1))
print('O erro é de: {}'.format(e))