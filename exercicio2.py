import math

''' 
    Felipe Amorim de melo
    Eng da Computação
    exercio sobre truncamento e arredondamento
'''

def arredondado(x):
    x += 0.000005
    return x
    # print("{:.5f}".format(x))


def truncado(x):
    return x
    # print("{:.5f}".format(x))

def imprime(x):
    print("valor real: {}".format(x))
    print("valor truncado: {:.6f}".format(truncado(x)))
    print("valor arredondado: {:.6f}\n".format(arredondado(x)))

valor = [math.sqrt(2),(1.0/9.0),math.pi,(1.0/7.0),(100.0/7.0)]

for i in valor:
    imprime(i)
    


