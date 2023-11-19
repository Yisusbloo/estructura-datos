#Divicion por restas
def diviporrestas(dividendo, divisor):
    cociente = 0
    for _ in range(int(dividendo // divisor)):
        dividendo -= divisor
        cociente += 1
    return cociente, dividendo

dividendo = float(input("Ingresa el dividendo: "))
divisor = float(input("Ingresa el diviso: "))

cociente, residuo = diviporrestas(dividendo, divisor)
print(f"La división de {dividendo} / {divisor} usando restas es:")
print(f"Cociente: {cociente}")
print(f"Residuo: {residuo}")