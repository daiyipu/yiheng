#实例01：用SymPy库函数求解出的雅克比矩阵的形式。

import sympy
m,n,i,j = sympy.symbols("m n i j")
m = i**4-2*j**3-1 #设置变量（符号）
n = j-i*j**2+5
funcs = sympy.Matrix([m,n])#矩阵的维度m,n
args = sympy.Matrix([i,j])
res = funcs.jacobian(args)#调用jacobian函数求解
print(res)

#实例02：Theano库实现雅克比矩阵的计算。
import theano
from theano import function, config, shared, sandbox
import theano.tensor as T
# 计算雅克比矩阵
x=T.dvector('x')
y=x**3+x**4
# 调用scan构建循环Graph
J,updates=theano.scan(lambda i,y,x:T.grad(y[i],x),sequences=T.arange(y.shape[0]),non_sequences=[y,x])
f1=function([x],J,updates=updates)
print("f1=",f1([5, 5]))

#实例03：Theano库实现海森矩阵的计算。
import theano
from theano import function, config, shared, sandbox
import theano.tensor as T
x=T.dvector('x')
# 计算hessian矩阵
y=x**3+x**4
cost=y.sum()
gy=T.grad(cost,x) #求梯度
# 调用scan构建循环Graph
H,updates=theano.scan(lambda i,gy,x:T.grad(gy[i],x),sequences=T.arange(gy.shape[0]),non_sequences=[gy,x])
f2=function([x],H,updates=updates)
print("f2=",f2([5, 5]))

