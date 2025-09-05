#Wk3 Lesson3 homework
def display_temperature(city, temperature):
    """Displays the temperature and the city name"""
    print(f"The temperature in {city} is currently {temperature} degrees")


display_temperature("London", 7)
display_temperature("New York", 12)


#Wk3 Lesson4 default values in functions
def display_full_name(first_name, last_name, middle_name=""):
    """Displays the full name based on the first, middle and last name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name  #so there are no spaces if they dont have a middle name

    print(full_name)


display_full_name("John", "Smith", "Jane")
display_full_name("John", "Smith")

#Wk3 Lesson4 challenge - create a function that has 3 parameters (city temp and humidity level) and display the following message:The temperature in London is 7 degrees with a humidity of 40%.If the humidity isn’t provided, display the following message:The temperature in New York is 10 degrees.Call this function twice. one time with humidity and one time without


def display_weather(city, temperature, humidity=""):
    """Display the following message:The temperature in London is 7 degrees with a humidity of 40%."""

    if humidity:
        print(
            f"The temperature in {city} is {temperature} degrees with a humidity of {humidity}%"
        )
    else:
        print(f"The temperature in {city} is {temperature} degrees")


display_weather("London", 7, 40)
display_weather("London", 7)


#Matts code lesson4 challenge with a message variable
def display_temperature(city, temperature, humidity=None):
    """Displays the temperature and humidity of a city."""

    message = f"The temperature in {city} is {temperature} degrees"
    if humidity:
        message = f"{message} with a humidity of {humidity}%"
    print(f"{message}.")


display_temperature("London", 7, 40)
display_temperature("New York", 7)


#return values in functions (functions return) wk 3 lesson 5
def full_name(first_name, last_name, middle_name=None):
    """Returns the full name of a person"""  #this is a docstring
    if middle_name:
        return first_name + " " + middle_name + " " + last_name
    else:
        return first_name + " " + last_name


name = full_name("John", "Smith")
print("The full name is " + name)
name = full_name("John", "Smith", "Jr")
print("The full name is " + name)


def fahrenheit(celsius):
    """Returns the Fahrenheit value of a Celsius temperature"""
    return celsius * 9 / 5 + 32


city = "Madrid"
current_celsius = 25
current_fahrenheit = fahrenheit(current_celsius)

print(
    f"It is currently {current_celsius}ºC ({current_fahrenheit}ºF) in {city}.")


#also
def fahrenheit(celsius):
    return celsius * 9 / 5 + 32


print(f"It is currently 15ºC ({fahrenheit(15)}ºF) in London.")


#Challenge - Create a function that returns the Fahrenheit value of a Celsius temperature.Display the following and use the function to calculate the Fahrenheit value: It is currently 15ºC (59ªF) in London.

def convert_to_fahrenheit(celsius):
    """Converts a Celsius value into Fahrenheit"""
    fahrenheit = (float(celsius) * 9 / 5) + 32

    return fahrenheit


def display_temperature(city_name, temperature):
    """Displays the temperature of a city"""
    fahrenheit_temperature = convert_to_fahrenheit(temperature)
    print(
        f"It is currently {temperature}ºC ({round(fahrenheit_temperature)}ºF) in {city_name.capitalize()}"
    )


#main code
city = input("What city are you in: ")
celsius_temp = input(f"Enter the temperature in {city.capitalize()}: ")

if city and celsius_temp:
    display_temperature(
        city, celsius_temp)  #pass in the variables city and celsius_temp
else:
    print("You must enter a city and/or temperature, please try again")
