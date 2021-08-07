#CICLO WHILE
# number = 7

# while True:
#     user_input = input("Would you like to play: (Y/n) ")
    
#     if user_input == "n":
#              break

#     user_number = int(input("Guess our number: "))
#     if user_number == number :
#         print("You guessed the correctly")
#     elif abs(number - user_number) == 1 :
#         print("You we're off by one")
#     else :
#             print("Sorry it's wrong")


#CICLO FOR

friends = ["Bob", "Anne", "Rolf", "Jen"]

for friend in range(4):
    print(f"{friend} is my friend")

###########################################

grades = [35, 67, 98, 100, 100]

total = sum(grades)
amount = len(grades)
print(total / amount)

#SUM REALIZA LA SUMA DE LOS ELEMENTOS DE GRADES, LEN CUENTA LOS ELEMENTOS DE GRADES TOTAL / AMOUNT = 400 / 5


#Ejercicio

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []

for number in numbers :
    if number %  2 == 0:
        evens.append(number)
        print(evens)

########################

user_input = input("Enter your choice: ")
if user_input == "a":
    print("Advanced")
elif user_input == "q" :
        print("Quite")