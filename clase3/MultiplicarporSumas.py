#Multiplicacion por medio de sumas

def multiporsumas(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
        print(resultado)
    return resultado
    

n1= float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))

producto = multiporsumas(n1, int(n2))
print(f"El resultado de {n1} * {n2} usando sumas repetidas es: {producto}")