if __name__ == '__main__':
    n = int(input("Leer n "))
    aux = n
    cont = 0
    while n > 0 :
        d = n%2
        n = int(n/2)
        cont += 1
        #print(d)

    print("T(n) = 2+t (t cantidad de iteraciones) por lo tanto siempre va a pasar que:")
    print("n < 2^t+1 ejemplo")
    print("n = ", aux , " y 2^t+1 = ", pow(2,cont+1))
    print(aux,"<",pow(2,cont+1))
    print("Por lo tanto la complejidad es O(log(n))")


