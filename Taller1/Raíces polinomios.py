# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:21:09 2023

@author: isabe
"""

import sympy as sym

c=2
x = sym.Symbol('x',Real=True)

funcion = ((3*(x**5))+(5*(x**4))-(1*(x**3)))

f = sym.lambdify([x],funcion,'numpy')
h = 0.01

def Deriv(f,x,h):
    a= (f(x+h)-f(x-h))/(2*h)
    return a


def Raiz_NewtonR(xi,f,df,h2):
    N = 0
    lista=[]
    while N<5:
        xn1= xi - (f(xi))/df(f,xi,h)
        if f(xn1)==0 and xn1-xi<h2:
            N+=1
            lista.append(xn1)
        xi=xn1
           
    return lista

print(Raiz_NewtonR(1,f,Deriv,h))