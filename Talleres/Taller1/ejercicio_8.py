from matplotlib import pyplot
import sympy as sy
import math


def f1(t):
    return math.cos(3*t)

def f2(t):
    return math.exp(t)

def graficar():
    t = range(-2,2)

    pyplot.plot(t, [f1(i) for i in t])
    pyplot.plot(t, [-f2(i) for i in t])

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    pyplot.xlim(-2, 2)
    pyplot.ylim(-3.5, 3.5)

    pyplot.savefig("output.png")
    pyplot.show()

def newton(a):
    t=sy.Symbol('t')
    f=2+sy.cos(3*t)-(2-sy.exp(t))
    g=t-f/sy.diff(f)
    u=a
    uant = 0
    cont = 0
    while u != uant:
        uant=u
        u=float(g.subs(t,u))
        cont +=1
    print("Por el metodo de newton ", u)
    

def biseccion(a):
    ini = 0
    fin = 0
    aux = a
    error = 0.00000020
    erroract = 0.00000002
    xi = 0.00000020
    xii = 0.00000000
    while aux < 2:
        xo = math.exp(aux)+ math.cos(3*aux)
        if(xo-aux>0.0001 and ini == 0):
            ini = aux
        elif (xo-aux<1):
            fin = aux
        aux += 1.000000
    while erroract < error:
        fa = math.exp(ini)+ math.cos(3*ini)
        fb = math.exp(fin)+ math.cos(3*fin)

        if ((fa*fb) < 0):
            xi = (ini+fin)/2
            fxi = math.exp(xi)+ math.cos(3*xi)
            erroract = (xii-xi)
            if (fxi == 0):
                print ("La raiz es: ",fxi,"con un error del: ",error)
                return
            else:
                if((fa*fxi)>0):
                    ini = xi
                    xii = xi
                elif((fb*fxi)>0):
                    fin = xi
                    xii = xi
    print("Por el metodo de biseccion ", xi ," con un error de: ",error)
    
if __name__== '__main__':
    a = -1.0000000
    graficar()
    newton(a)
    biseccion(a)
    


