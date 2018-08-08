from matplotlib import pyplot
import math

## parte (a)
def funcion(x):
    return (5*x)-(math.exp(x))-1

## parte (b)
def grafico():
    t = range(-2,4)

    pyplot.plot(t, [funcion(i) for i in t])

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    pyplot.xlim(-3, 4)
    pyplot.ylim(-5, 5)

    pyplot.savefig("output.png")
    pyplot.show()

## parte(c)
def ecuacion_equivalente(x):
    return ((math.exp(x))+1)/5

def converge(x):
    i = ecuacion_equivalente(x)
    i1 = ecuacion_equivalente(i)
    i2 = ecuacion_equivalente(i1)
    i3 = ecuacion_equivalente(i2)
    if ((i1-i) > 0):
        if((i1-i) < (i2-i1) and (i2-i1) < (i3-i2)):
            converge = False
        elif ((i1-i) > (i2-i1) and (i2-i1) > (i3-i2)):
            converge = True
    elif((i1-i) < 0):
        if(((i1-i)*(-1)) < ((i2-i1)*(-1)) and ((i2-i1)*(-1)) < ((i3-i2)*(-1))):
            converge = False
        elif (((i1-i)*(-1)) > ((i2-i1)*(-1)) and ((i2-i1)*(-1)) > ((i3-i2)*(-1))):
            converge = True

    return converge

## parte (d)
def iteraciones(a):
    x = a
    error = []
    for i in range(0,5):
        x1 = x
        x = ecuacion_equivalente(x1)
        err = abs(x-x1)
        error.append(err)

    print("Iteracion 5",x)
        
    res = 0
    for x in range(0,len(error)-1):
        res += error[x+1]/error[x]
    res = res / (len(error)-1)
    print("Error de truncamiento " + str(res)) 
            
if __name__== '__main__':
    grafico()
    x1 = 0.4
    x2 = 2.6
## parte (c) Intervalo de convergencia (-inf,ln(4))
    if(converge(x1)):
        iteraciones(x1)
    if(converge(x2)):
        iteraciones(x2)
  
