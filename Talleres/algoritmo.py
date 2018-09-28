
def calculo(x):
    res = (pow(x,3))+(4*(pow(x,2)))-(10)
    return res

def raiz_funcion(inicio,fin,cantidad):

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

    if(inicio < 0):
        division = ((inicio*-1) + fin) / cantidad
    else:
        division = (inicio + fin ) / cantidad
    
    
    a = inicio
    b = division
    while erroract < error:
        fa = calculo(a)
        fb = calculo(b)

        if ((fa*fb) < 0):
            xi = (a+b)/2
            fxi = calculo(xi)
            erroract = (xii-xi)
            if (fxi == 0):
                print ("La raiz es: ",fxi,"con un error del: ",error)
                return
            else:
                if((fa*fxi)>0):
                    a = xi
                    xii = xi
                elif((fb*fxi)>0):
                    b = xi
                    xii = xi
        elif(cont <=cantidad):
            a = b
            b = b + division
        else:
            print("La raiz no esta en el intervalo")
        cont= cont+1
    print("El valor mas cercano a la raiz es: ",xi," con un error de: ",error)
    print("Cantidad de iteraciones para encontrar valor es: ", cont)

if __name__ == '__main__':
    a = 1.10
    b = 1.5
    cantidad = 4
    raiz_funcion(a,b,cantidad)
