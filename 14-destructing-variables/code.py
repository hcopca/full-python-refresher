people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for person in people:
    print(f"Name: {person[0]}, Age:{person[1]}, Profeession: {person[2]}")

    person = ("Bob", 42, "Mechanic")
    #El guion es para ignorar la variable
    name, _, profession, = person
    print(name, profession)

    ##
##El asterisco es para definir sí es la cabeza o la cola
    head, *tail = [1, 2, 3, 4, 5]
    print(head)
    print(tail)