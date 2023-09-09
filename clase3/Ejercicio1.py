edades = [35, 12, 15, 20, 40]

for n in edades:
    print(f"edades {n}" )

    def promedio_edades(edades):
        suma = 0
        for n in edades:
            suma = suma + n
        return suma / len(edades)

promedio = promedio_edades(edades)
print(f"El promedio de las edades es: {promedio}")