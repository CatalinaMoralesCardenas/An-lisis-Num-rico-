def cont_digitos(n):
    cant = 1
    while n > 9:
        n = n / 10
        cant = cant + 1
    return cant

def digitos(n):
    return list(map(int, str(n)))

def error(n, capacidad):
    exponente = cont_digitos(n)
    notacion = int(n*(pow(10,exponente-1)))
    arreglo = digitos(notacion)

    truncamiento = 0
    for i in range(capacidad,len(arreglo)):
        truncamiento = (truncamiento*10) + arreglo[i]

    valor = truncamiento/10
    error = exponente-capacidad
    
    print("El error de redondeo es ", valor , "x10^",error)
        
        
    
if __name__ == "__main__":
    n = float(input("Ingrese el numero que desea almacenar "))
    capacidad = int(input("Ingrese la capacidad de digitos que puede almacenar su dispositivo "))
    error(n,capacidad)

