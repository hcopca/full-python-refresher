friends = {"Bob", "Ann", "Rolf"}
abroad = {"Bob", "Ann", "Mario"}

#difference resta los elementos de del set al otro set con la propiedad difference.
local_friends = friends.difference(abroad)
# print(local_friends)

#union suma los elementos en un set
amix = friends.union(abroad)
# print (amix)


#Ejercicio de intersection, este devuelve los elementos que se encuentran en dos set distintos.

art = {"Bob", "Jean", "Charly", "Rolf"}
sciencie = {"Bob", "Jean", "Adam", "Anne"}

both = art.intersection(sciencie)
# print(both)

#Ejercicio 
my_list = [20, 50, 30]
my_tuple = ("Hugo",)
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}
print(my_tuple)