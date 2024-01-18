''' Este Programa es el B y el cual convierte un número del sistema decimal a Binario, Octal 
y Hexagesimal sin importar si es positivo, negativo o si se tienen numeros despues
del punto decimal. 
Se debe tomar en cuanta que se sigue la norma de "Signo - Magnitud" por lo cual el primer
número representa al signo siendo 1 "negativo" y 0 "positivo" la segunda parte representa
a los numero enteros y la ultima parte representa a los numero fraccionarios"'''

def convertidor(n,m):
    #"El signo" esté descrito como 1 = negativo y 0= positivo ya que sigue la norma "Signo - Magnitud"
    # sin importar que sistema sea.
    if n < 0:
        n = -(n)
        s = [1]
    else:
        s = [0]
    s = ''.join(str(x) for x in s)

    #Parte fraccionaria: ubicada al final del numero
    d = n % 1
    dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'} 
    if d > 0:    
        e = []
        i = 0
        #dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'} 
        while i <= 10:
            d1 = d * m
            e1 = round(d1 // 1)
            if e1 >= 10:
                e1 = dic.get(e1)
            e.append(e1)
            d = d1 % 1
            i += 1
        e = ''.join(str(x) for x in e)
    else:
        e = "---> No hay decimales"
    

    #parte entera: segunda parte del número
    n = round(n // 1)
    if n == 0:
        print("No hay parte entera")   
    r = []
    #dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'} 
    while n > 0:
        x = n % m
        if x >= 10:
            x = dic.get(x)
        r.append(x)
        n = n //m
    r.reverse()
    r =''.join(str(x) for x in r)
    print(f"El numero es el siguiente: {s} {r} {e}")

print("---En Sistema binario---")
convertidor(256,2) 
print("---En Sistema Octal---")
convertidor(256,8)
print("---En Sistema Hexadecimal---")
convertidor(256,16)



