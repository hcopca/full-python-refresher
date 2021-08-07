user_age = int(input("Enter your age: "))
# YA NO ES NECESARIO CONVERTIR EL EL RESULTADO DEL INPUT EN USER AGE A NUMERO PORQUE YA SE AGREGA EL INT EN LA MISMA VARIABLE
# years = int (user_age)
# months = user_age * 12
#EJERCICIO DE CONVERTIR A SEGUNDOS LOS AÑOS DE VIDA
# print (f"Your age, {user_age}, is equal to {months} months.")
secs = ((user_age * 365) * 24)*60
print (f"Your age, {user_age}, is equal to {secs} seconds.")