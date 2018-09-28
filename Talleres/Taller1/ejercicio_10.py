import sympy as sy
import math 

## a  = valor inicial
## ma = cantidad de iteraciones
def metodo_newton(a,ma):
    x = sy.Symbol('x')
    fun = (pow(x,3))-(6*(pow(x,2)))+(10*x)-2
    g = x-fun/sy.diff(fun)
    r = a
    for i in range(ma):
        r = float(g.subs(x,r))
        print("valor aprox por metodo de newton es = ", r)

if __name__ == '__main__':
    metodo_newton(0,4)    
