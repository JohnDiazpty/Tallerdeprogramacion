Nombre = input("Cuál es tu nombre ")
edad = int(input("Cuál es tu edad "))

Nota1 = float(input("¿Cuál es la nota 1 "))
Nota2 = float(input("¿Cuál es la nota 2 "))
Nota3 = float(input("¿Cuál es la nota 3 "))

resultado = (Nota1 + Nota2 + Nota3) / 3

print("Nombre:", Nombre)
print("Edad:", edad)
print("Promedio:", resultado)

if resultado >= 71:
    print("Aprobado")
else:
    print("No aprobado")