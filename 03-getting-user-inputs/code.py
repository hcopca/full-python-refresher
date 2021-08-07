# name = input("Enter your name: ")
# print(f"Tu nombre es {name}")

#Size Input

size_input = input("How big is your house (in square feet: ")
# Lo que hace int es convertir la string en un numero para poder utilizarlo en una operación
square_feets = int(size_input) 
square_meters = square_feets / 10.8
print(f"{square_feets} square feets is {square_meters:.2f} square metres")
# Lo que hace el :.2f es unicamente imprimir las dos primeras decimales.


# Ejercicio web
x = 4863.4343091
print(f"{x:.6}") 
print("{:.6}".format(x))