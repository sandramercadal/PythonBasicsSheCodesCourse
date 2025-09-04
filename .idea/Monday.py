from tkinter.font import names

print("Hello World")
print("Miss Sunshine; Mr Men!")
print('👌🏾 overview')

city = input("Enter the name of a city: ")
temperature = input(f"Enter the temperature in {city}: ")

if city and temperature:
    temperature = int(temperature)

    if temperature > 20:
        print(f"It is currently warm in {city} with a temperature of {temperature} degrees.")
    elif temperature > 10:
        print(f"It is currently chilly in {city} with a temperature of {temperature} degrees.")
    else:
        print(f"It is currently cold in {city} with a temperature of {temperature} degrees.")
else:
    print("Please try again and enter a city and temperature")


def say_hello_world():
        print("hello_world_whoop")

happy = input ("Are you happy?(yes/no)")
if happy == 'yes':
        say_hello_world()


def say_hello_world2():
    name = input("What is your name?")
    if name:
        print(f"Hello {name.capitalize()}!")
    else:
        print("You dont have a name")

say_hello_world2()


#Create a function asking for the city where you are and the current temperature and display this message:
#You are in Lisbon and it is currently 17ºC.
#Call this function twice.
#Bonus point: Display an error message if the user doesn’t enter a city or a temperature

def welcome_user():
    print("Welcome to my amazing weather app!")
def which_city_and_temp():
    city = input ("What city are you in: ")
    temperature = input ("What is the temperature today: ")

    if not temperature or not city:
        print ("Please enter a city and a temperature")
    else:
        print(f"You're in {city} and it's {temperature}ºC")
welcome_user()
#call function twice
which_city_and_temp()
which_city_and_temp()

#We dont know whats inside name we call it with the string Matt
def greet_user(name):
    """Welcome the user"""
    print(f"Hello {name}")

greet_user("Matt")

"""Helps you debug"""
help(greet_user)

def greet_user_again(first_name, last_name):
    """Welcome the user"""
    print(f"Hello {first_name} {last_name}")

greet_user_again("Matt", "Delac")

"""Homework lesson 3 wk 3"""
def enter_city_and_temp(city, temperature):
    """Print this"""
    print(f"You are in {city} and its {temperature}ºC")

enter_city_and_temp("Sydney", "12")
enter_city_and_temp("Madrid", "17")





