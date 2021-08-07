users = [
    (0, "Bob", "password"),
    (1, "Joss", "longpass"),
    (2, "Angie", "shortpass"),
    (3, "Mich", "1222"),
]

username_map = {user[1]: user for user in users}

username_input = input("Enter your username :")
password_input =  input("Enter your password :")

_, username, password = username_map[username_input]

if password_input ==  password:
    print("Login")
else:
    print("Logout")


    ####EJERCICIO 

    # Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    "name":"Jose",
    "school":"Computing",
    "grades":(66,77,88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =   data["grades"]
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])

    return total / count