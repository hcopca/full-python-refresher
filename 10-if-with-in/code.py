movies_watched = {"The matrix", "The greenbook", "Her"}
user_movie = input ("Enter something movie: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too")
else :
    print("I haven't watched that yet")


    ############################MAGIC NUMBER#########################

    number = 7
    user_input = input("Enter 'y' if you would like to play: ").lower()

    if user_input == "y" :
        user_number = int(input("Guess our number: "))
        if user_number == number :
            print("You guessed the correctly")
        elif abs(number - user_number) == 1 :
            print("You we're off by one")
        else :
                print("Sorry it's wrong")
