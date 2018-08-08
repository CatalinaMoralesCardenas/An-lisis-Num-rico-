def calculo(x,funcion):
    a = funcion[0]*(pow(x,3))
    b = funcion[1]*(pow(x,2))
    c = funcion[2]*x
    res = a + b + c
    return res

def calculoDerivada(x,derivada):
    a = derivada[0]*(pow(x,2))
    b = derivada[1]*x
    c = derivada[2]
    res = a + b + c
    return res

def biseccion(inicio,fin,cantidad,largo,ancho):

    a = 0.00000020
    b = 0.00000020
    fa = 0.00000020
    fb = 0.00000020
    xi = 0.00000020
    fxi = 0.00000020
    error = 0.00000020
    erroract = 0.00000002
    division = 0.00000000
    xii = 0.00000000
    cont = 0
    
    funcion = [4]
    funcion.append(-2*(largo+ancho)) 
    funcion.append(largo*ancho)
    
    if(inicio < 0):
        division = ((inicio*-1) + fin) / cantidad
    else:
        division = (inicio + fin ) / cantidad
    
    
    a = inicio
    b = division
    while erroract < error:
        fa = calculo(a,funcion)
        fb = calculo(b,funcion)
        alfa = fa-1000
        omega = fb-1000

        if ((alfa*omega) < 0):
            xi = (a+b)/2
            fxi = calculo(xi,funcion)
            gamma = fxi-1000
            erroract = (xii-xi)
            if (fxi == 0):
                print ("La medida a cortar para los lados de los cuadrados es : ")
                print (xi," con un error de: ",error)
                return
            else:
                if((alfa*gamma)>0):
                    a = xi
                    xii = xi
                elif((omega*gamma)>0):
                    b = xi
                    xii = xi
        elif(cont <=cantidad):
            a = b
            b = b + division
        cont= cont+1
    print("La medida a cortar para los lados de los cuadrados es : ")
    print(xi," con un error de: ",error, " por el metodo de biseccion")

def funcionDerivada(funcion):
    d = funcion[0]*3
    derivada = [d]
    derivada.append(funcion[1]*2)
    derivada.append(funcion[2])
    return derivada

def newton(largo,ancho):
    funcion = [4]
    funcion.append(-2*(largo+ancho)) 
    funcion.append(largo*ancho)
    derivada = funcionDerivada(funcion)
    res= 0.00005
    xn = 0.50000
    xi = 0.00001
    c = 0.0000002
    while ((res-xi)>0.0000002):
     j = (calculo(xn,funcion))-1000
     k = calculoDerivada(xn,derivada)
     xi = xn
     res = xn-(j/k)
     xn = xn + 0.0001
    print("La medida a cortar para los lados de los cuadrados es : ")
    print(xn, " por el metodo de newton rhapson con un error de", res-xi)


if __name__ == "__main__":
    largo = float(input("Ingrese el largo de la caja "))
    ancho = float(input("Ingrese el ancho de la caja "))
    a = 0
    b = ancho/2
    cantidad = 2
    biseccion(a,b,cantidad,largo,ancho)
    newton(largo,ancho)
