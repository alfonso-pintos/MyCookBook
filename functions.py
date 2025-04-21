def greet_user():
    print("Welcome to the guessing game!")

def greet_user_by_name(name = "User", greeting = "Hello"):
    print(greeting + ", " + name)


def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value


# greet_user_by_name(name=  input("What is your name? "), greeting = "Welcome")
# greet_user_by_name()
# greet_user_by_name("Alfonso", "Welcome Back")
# greet_user_by_name(name="Fonsi", greeting="Welcome Back")


eleven_cubed = cube(11)
print(eleven_cubed)