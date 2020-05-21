import math

def erro(x, h):
    return (h ** 2 / 2) * -1 * math.cos(x) + (h ** 3 / 6) * math.sin(x) + (h ** 4 / 24) * math.cos(x)


def erroCentral(x, h):
    return erro(x, h)**2


def fx(x):
    return 10 * math.cos(x)


def diferencas(h):
    dfdx1 = (fx(x+h) - fx(x)) / h + erro(x, h)
    dfdx2 = (fx(x) - fx(x-h)) / h + erro(x, h)
    dfdx3 = (fx(x+h) - fx(x-h)) / (2 * h) + erroCentral(x, h)

    print("passo : {}".format(h))
    print("diferenca progressiva: {} || Erro: {}".format(
                                dfdx1, ((solucao - dfdx1)*100)/solucao))
    
    print("diferenca atrasada: {} || Erro: {}".format(
                                dfdx2, ((solucao - dfdx2)*100)/solucao))

    print("diferenca central: {} || Erro: {}".format(
                                dfdx3, ((solucao - dfdx3)*100)/solucao))

h1 = 0.1
h2 = 0.02
h3 = 0.0001
x = math.pi / 6

solucao = -10 * math.sin(x)
print(solucao)

diferencas(h1)
diferencas(h2)
diferencas(h3)