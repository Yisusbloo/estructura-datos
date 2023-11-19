#Ejemplo de funciones con ciclos

edades =[35,12,15,40,20]

def promedio_edades(edades):
    suma=0
    edades =[35,12,15,40,20]
    for n in edades:
        suma =suma+n
    return suma / len(edades) #len sirve para contar cuantos datos existen dentro de un arreglo

promedio = promedio_edades(edades)
print(f"el promedio de las edades es: {promedio}")#La f sirve para en un print mostrar datos y texto dentro de las comillas.
    