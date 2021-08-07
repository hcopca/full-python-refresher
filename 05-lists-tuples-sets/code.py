#Se puede modificar, agregar, eliminar etc.
l = ["Bob", "Rolf", "Anne"]
#No se pueden modificar valores, borrar, agregar etc
t = ("Bob", "Rolf", "Anne")
#En un set, el orden es aleatorio por lo que si se intenta acceder así t[0], no obtendrá resultado.
s = {"Bob", "Rolf", "Anne"}

#Para cambiar el primer valor de un list se puede hacer de la siguiente forma, esto no se puede hacer en un tuple o set
l[0] = "Smith"
print(l)
#El resultado será Smith, Rolf, Anne, sustituyendo a Bob

#Para agregar un elemento al final de la lista se realiza con "append" Ejemplo: No se puede hacer en un tuple o set.

l.append("Copca")
print(l)

#Para eliminar un elemento es con remove. Escribiendo el nombre del elemento a borrar.
l.remove("Anne")
print(l)

#Es posible agregar un elemento a set con la propiedad add, pero no es posible añadir elementos repetidos en el.

s.add("Seetkof")
print(s)