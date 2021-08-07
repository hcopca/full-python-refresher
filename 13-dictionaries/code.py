friends = [
    {"name": "Rolf", "age" : 24},
    {"name": "Adam", "age" : 30},
    {"name": "Anne", "age" : 27}
]

#Acceder entre los elementos de una lista
print(friends[0]["name"])

#######################INTERAR DENTRO DE DICCIONARIOS################


student_atendences = {"Rolf": 96, "Bob": 80, "Anne": 100}
# for student in student_atendences:
#     print(student)

# for student in student_atendences in student_atendences.items():
#     print(f"{student}: {student_atendences[student]} ")

if "Bob" in student_atendences:
    print(f"Bob: {student_atendences['Bob']}")
else:
    print("Bob is not a student")


##Sumar los numeros y sacar promedios de student_atendeces

attendance_value = student_atendences.values()
print(sum(attendance_value)/len(attendance_value))