# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:19:22 2023

@author: isabe
"""

from urllib.request import urlopen
import numpy as np
import matplotlib.pyplot as plt

r=urlopen('https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/EstrellaEspectro.txt')
f=r.read()

cu=(f.decode()).split()

lon=len(cu)

matriz=np.zeros((int((lon)/2),2))
                

for i in range(0,lon):
    
    co=int(i/2)
    
    if i%2==0:
        
        matriz[co,0]=float(cu[i])
        
    else:
        matriz[co,1]=float(cu[i])
        
        
maximos=[]  
posicion=[]
    
for x in range(1,(len(matriz)-1)):
    
    n1=matriz[(x-1,1)]
    n2=matriz[(x+1,1)]
    n3= matriz[x,1]
    m1= matriz[x,0]
   
   
    if n1<n3 and n3>n2:
        
        maximos.append(n3)
        posicion.append(m1)

matriz_puntos=np.zeros((len(maximos),2))

for x in range(0,len(maximos)):
    
    matriz_puntos[x,0]=posicion[x]
    matriz_puntos[x,1]=maximos[x]
    
    
plt.scatter(matriz_puntos[:,0],matriz_puntos[:,1],color='r')
plt.plot(matriz[:,0],matriz[:,1],color='b')