import numpy as np
import matplotlib.pyplot as plt


lista = np.linspace(0,20,20)
fibonac = np.zeros(20)
cero = 0
uno = 1

aureo = np.empty(20)
aureo.fill((1+(5**0.5))*0.5)

fibonac[0] = cero
fibonac[1] = uno

def fibonacci(f1,f2):
    f = f1+f2
    return f

def Ciclo():
    for i in range (2,20):
        fibonac[i] = fibonacci(fibonac[i-1],fibonac[i-2])

def Aureo(Fib):
    aur = np.zeros(19)
    aur[0] = 0
    for i in range(1,19):
        aur[i]=Fib[i+1]/Fib[i]
    return aur

Ciclo()
est_aureo = Aureo(fibonac)
fig = plt.figure( figsize=(8,4) )
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(lista, fibonac,label='Sucesión de Fibonacci')
ax2.plot(lista[0:19],est_aureo,label="Estimación del Número Aureo")
ax2.plot(lista,aureo,'--', label="Número Aureo")
ax1.legend()
ax2.legend(loc=4)