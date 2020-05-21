import matplotlib.pyplot as plt


def condInicial(x):
    return x * (x-1)


def Tproximo(t, t1):
    i = 0
    for i in range(0, len(t)):
        if i == 10:
            t1.append(t[i] + 0.001 * (t[i-1] - 2*t[i] + 0))
            break
        else:
            t1.append(t[i] + 0.001 * (t[i-1] - 2*t[i] + t[i+1]))
        i += 1


t0 = []

for i in range(0, 110, 10):
    t0.append(condInicial(i))

print(t0)

t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
t7 = []
t8 = []
t9 = []
t10 = []

Tproximo(t0, t1)
Tproximo(t1, t2)
Tproximo(t2, t3)
Tproximo(t3, t4)
Tproximo(t4, t5)
Tproximo(t5, t6)
Tproximo(t6, t7)
Tproximo(t7, t8)
Tproximo(t8, t9)
Tproximo(t9, t10)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)
print(t9)
print(t10)

T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.plot(T, t0, label='T0(t)')
plt.plot(T, t1, label='T1(t)')
plt.plot(T, t2, label='T2(t)')
plt.plot(T, t3, label='T3(t)')
plt.plot(T, t4, label='T4(t)')
plt.plot(T, t5, label='t5(t)')
plt.plot(T, t6, label='T6(t)')
plt.plot(T, t7, label='T7(t)')
plt.plot(T, t8, label='T8(t)')
plt.plot(T, t9, label='T9(t)')
plt.plot(T, t10, label='T10(t)')
plt.xlabel('tempo (t)')
plt.ylabel('valores Temperatura (t)')
plt.legend()
plt.show()
