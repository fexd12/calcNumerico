import math

# colocar o valor de x a ser calculado e y quantas integracoes fazer
def exp(x,y):
    i = 0
    j = 0

    while i <= y:
        j += (math.pow(x,i)) / math.factorial(i)
        i += 1
    
    return j

# colocar o valor de x a ser calculado e y quantas integracoes fazer
def seno(x,y):
    i = 0
    j = 0

    x= x/180*math.pi

    while i <= y:
        j += (math.pow(-1,i) / math.factorial(2 * i + 1)) * math.pow(x,(2 * i + 1))
        i += 1
    return j


# colocar o valor de x a ser calculado e y quantas integracoes fazer
def cosseno(x,y):
    i = 0
    j = 0

    x= x/180*math.pi

    while i <= y:
        j += (math.pow(-1,i) / math.factorial(2 * i)) * math.pow(x,(2*i))
        i += 1
    return j

def erro(esperado,obtido):
    return math.fabs(((obtido - esperado) / esperado)) * 100

e = int(input("\ndigite um valor para e "))
sen = int(input("digite um valor para sen "))
cos = int(input("digite um valor para cos "))

print("\nValor real de e eh: {}".format(math.exp(e)))
print("valor calculado de e para 1 interação eh: {} e para 10 eh de: {}".format(exp(e,1),exp(e,10)))
print("Erro obtido de e para 1 interação eh: {}'%' e para 10 eh de {}'%' \n".format(erro(math.exp(e),exp(e,1)),erro(math.exp(e),exp(e,10))))

print("Valor real de seno eh: {}".format(math.sin(sen)))
print("valor calculado de seno para 1 interação eh: {} e para 10 eh de: {}".format(seno(sen,1),seno(sen,10)))
print("Erro obtido de seno para 1 interação eh: {}'%' e para 10 eh de {}'%'\n".format(erro(math.sin(sen),seno(sen,1)),erro(math.sin(sen),seno(sen,10))))

print("Valor real de cosseno eh: {}".format(math.cos(cos)))
print("valor calculado de cosseno para 1 interação eh: {} e para 10 eh de: {}".format(cosseno(cos,1),cosseno(cos,10)))
print("Erro obtido de cosseno para 1 interação eh: {}'%' e para 10 eh de {}'%'\n".format(erro(math.cos(cos),cosseno(cos,1)),erro(math.cos(cos),cosseno(cos,10))))