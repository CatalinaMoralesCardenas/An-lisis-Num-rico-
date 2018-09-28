def hornerC (funcion, t, xo):
    respuesta = funcion[0]
    contador = 0
    for i in range (1, t+1):
         respuesta = respuesta*xo + funcion[i]
         contador=contador+2
    print ("La respuesta es ", respuesta," el numero de operaciones usadas fue ", contador)

def hornerDerivada (funcion, t, xo):
    respuesta = funcion[0]*t
    aux = t-1
    contador = 0
    for i in range (1, t):
         respuesta = respuesta*xo + (funcion[i]*aux)
         aux = aux-1
         contador=contador+2
    print ("La respuesta para la derivada es ", respuesta," el numero de operaciones usadas fue ", contador)

if __name__ == "__main__":
     t = int(input("Ingrese el grado del polinomio a evaluar "))
     funcion = []
     for x in range (0, t+1):
         aux = float(input ("Ingrese el coeficiente de la variable de mayor a menor grado "))
         funcion.append(aux) 
     xo = float(input("Ingrese el valor en el que se va a evaluar la funcion "))
     hornerC(funcion, t, xo)
     hornerDerivada(funcion, t, xo)
