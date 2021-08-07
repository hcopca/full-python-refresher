#Multiplicar una lista de numeros x2 y agregarlos en una nueva.
numbers = [1, 3, 5]

double = [ x * 2 for x in numbers]
print(double)

#Extraer los nombres de una lista que comiencen con S

# friends = ["Bob", "Sam", "Sarah", "Soil" "Pepe"]
# start_with_S = []

# for friend in friends:
#     if friend.startswith("S"):
#          start_with_S.append(friend)

# print(start_with_S)

##codigo de arriba simplificado 

friends = ["Bob", "Sam", "Sarah", "Soil" "Pepe"]
start_with_S = [friend for friend  in friends  if friend.startswith("S")]

print(start_with_S)