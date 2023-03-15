# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 18:51:04 2023

@author: isabe
"""

import sympy as sp

x = sp.Symbol('x')
funcion = 3 + 5*x + x**2

N = 3
a = []
for n in range(N):
    if n == 0:
        a_n = sp.integrate(funcion, (x, -1, 1))
    else:
        P_n = sp.legendre(n, x)
        integral = sp.integrate(funcion * P_n, (x, -1, 1))
        a_n = (2*n + 1)/(n*(n+1)) * integral
    a_n = sp.ratsimp(a_n)
    a.append(a_n)

c1 =  a[0]/2
c3 =  a[2]* 3
print( str(c1) + 'P_0(x)  ' + str(a[1]) + 'P_1(x)  ' + str(c3) + 'P_2(x)' )