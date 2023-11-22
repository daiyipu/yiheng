#coding:utf-8
import sympy
sympy.init_printing()
from sympy import oo
# 1.求sin(a) / a在a=0处的极限
a = sympy.Symbol('a')
b = sympy.sin(a) / a
result = sympy.limit(b,a,0)
print('sin(a) / a在a趋近于0处的极限:',result)

#2.求[(n+3)/(n+2)]^n ,n趋紧无穷大时的极值
n = sympy.Symbol('n')
y = ((n+3)/(n+2))**n
print ( '[(n+3)/(n+2)]^n ,n趋紧无穷大的极值：',sympy.limit(y, n, sympy.oo) )
