import math
import numpy as np

def f(x,y):
    return (- 0.2 / 1) * (x * x) - 9.81

h= 0.01
N = 1000
x = np.empty(N)
y = np.copy(x)
x[0] = 0
y[0] = 0

for i in np.arange(N-1):
    x[i+1] = x[i] + h  
    y[i+1] = y[i] + h * f(x[i],y[i])

for d in range(1000):
    print("velocidade:{:.2f} tempo: {}".format(y[d],x[d]))


