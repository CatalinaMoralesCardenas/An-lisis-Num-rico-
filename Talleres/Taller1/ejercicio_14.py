from matplotlib import pyplot
import sympy as sy
import math

## c)
def raiz(a,b,e):
    x=a
    cambio = 0
    d = 1
    f=0
    while d > e:
        f=pow(x,2)-1
        if(f < 0):
            cambio = 1
        elif(f > 0):
            cambio = 0
        if(cambio == 0):
            d = (b-a)/10
            x += d
        if(cambio == 1):
            d = d/10
            x -= d
    return x

if __name__== '__main__':
    print("La raiz aprox es ", raiz(-1.2,1.2,0.1))
    
    
    
