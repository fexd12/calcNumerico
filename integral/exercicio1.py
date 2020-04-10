import math

def fx(x):
    return (6*x-5)**(1/2)

def integral(x):
    return (6*x-5)**(3/2)/9

def area(a,b):
    return (fx(a) + fx(b))*(b-a)*0.5

def erro(a,b, n):
    return ((b-a)**3) * maximo(a, b, n) * (1/(12*(n**2)))

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

n = 100 
ini = 1.0
fim = 9.0
n_div = (fim - ini)/ n 
print('tamanho do passo {}'.format(n_div))

a = ini 
b = ini + n_div

resultado = 0
c = 0
while True:
    if(a >= fim):
        break
    resultado += area(a,b)
    a = b
    b += n_div
    c += 1

print('A integral de f(x): {}'.format(resultado * -1))
e = math.fabs(erro(ini, fim, n))
print('O erro é de: {}'.format(e))