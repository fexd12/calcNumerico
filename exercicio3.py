import math

"""
    Felipe Amorim de melo
    Eng da Computação
    Exercicio Teorema de Bolzano - Bissecção
"""

def bissecao(f, a, b, TOL):  
    m = (a+b)/2

    if math.fabs(b-a) < TOL:
        return m
    
    if f(m) == 0:
        return m
    
    if f(m) * f(a) < 0:
        return bissecao(f,a,m,TOL)
    else:
        return bissecao(f,m,b,TOL)
    
def a(x):
    return x**x + 0.96*x - 2.08

def b(x):
    x = x/180*math.pi
    return 1 / math.sin(x) - math.tan(x)

def c(x):
    return (math.e**-x) - math.log(x)

def d(x):
    return x - 2.7 * math.log(x)

def e(x):
    y = x/180*math.pi
    return math.log(x) - math.tan(y)

print("Exercicio a {}".format(bissecao(a,1.02,1.06,1e-6)))

print("Exercicio b {}".format(bissecao(b,0.73,0.78,1e-6)))

print("Exercicio c {}".format(bissecao(c,1.3,1.35,1e-6)))

print("Exercicio d {}".format(bissecao(d,2.4,3.2,1e-6)))

print("Exercicio e {}".format(bissecao(e,1,2,1e-6)))

    