from timeit import default_timer 

def fibRecursivo (n): # Define la funcion recursiva
    if n == 0:
        return 0
    elif n == 1:
        return 1         
    else:
        return (fibRecursivo(n-1) + fibRecursivo (n-2))
    

def fibItereativo (n): # Define funcion iterativa
    
    a = 0
    b = 1
    for k in range (n):
        inicio = default_timer()
        c = a + b
        print (f"n = {k} -> {a}")
        fin = default_timer()
        a = b
        b = c
        print (f"tiempo = {fin-inicio}")
    return b

print ("\n\n##### Numero de Fibonacci #####")

n = 40 # Valor solicitado, en este caso dado internamente aunque puede ser solicitado al usuario

print ("\n>>> Metodo Iterativo <<<\n" )

fibItereativo(n)

print ("\n>>> Metodo Recursivo <<<\n" )

for k in range (n):
    inicio = default_timer()                #inicia el tiempo (cronometro)"
    print (f"n = {k} -> {fibRecursivo(k)}")
    fin = default_timer()                      #se cierra el cronometro para el tiempo"
    print (f"tiempo = {fin-inicio}")