name = 'Matt'
print(name)
message = 'Good morning'
print(message)
first_name = 'Matt'
last_name = 'Delac'
print(first_name)
print(last_name)
first_name = 'Matthieu'
print(first_name)
number_of_pets = 2
print(number_of_pets)

hometown_county_of_birth = 'Spain'
print(hometown_county_of_birth)

#Integer
months = 12
print(months)

#Float
pi = 3.14
print(pi)

#Arithmetic
print(2 + 2)
print(2**2)

a = 10
b = 3
print(a * b / 2)

#Basis functions same as 2 to the power of 3
pow(2, 3)
print(pow(2, 3))

absolute = abs(-10)
print(absolute)

rounded_pi = round(pi)
print(rounded_pi)

rounded_pi = round(pi, 2)
print(rounded_pi)

price = 99
discount = 15
discounted_price = price - price * discount / 100
print(round(discounted_price))

hometown_county_current = 'London'
print(hometown_county_current)
country = 'England'
print(country)
print(country[0:3])  #access the first 3 characters
sentence = (
    f" I live in {hometown_county_current} in {country} which is abbreviated to {country[0:3].upper()}"
)
print(sentence)

hometown = "Madrid"
print(hometown)
country = "Spain"
print(country)

origin_sentence = f"I am from {hometown}, in {country}."
country_acronym = country[0:3].upper()
short_country_sentence = f"The first three letters of my country are {country_acronym}."

print(f"{origin_sentence} {short_country_sentence}")

current_temperature_in_celsius = 25
print(current_temperature_in_celsius)
current_temperature_in_fahrenheit = current_temperature_in_celsius * 9 / 5 + 32
print(round(current_temperature_in_fahrenheit))

name = "hi"
sentence = "it's sunny today"

print(len(name))

print(name[1])  #access the second character
print(name[0:4])  #access the first 4 characters

print(name + " " + sentence)
print(name + " " + sentence.capitalize())
print(name + " " + sentence.upper())

print("hello")
sentence = sentence.upper()
print(sentence)
print("Hello".strip("o"))  #remove the O = Hell
print("Hello".replace('l', 'x'))  #Hexxo
print("Hello".count("l"))

print(f'{name} {sentence}')
print(f"Good morning {name} {sentence}")

temperature = "12"
print(type(temperature))  #string
number = 12
print(type(number))

temperature = int(temperature)  #convert to integer
print(int(temperature) + 10)

temperature = "12.5"
temperature = float(temperature)  #convert to float
print(temperature + 10)

temperature = 12
temperature = str(temperature)  #convert Int or float to string
print("It is currently" + " " + temperature + "degrees")

#input() always returns a string
#name = input("What is your name? ")
#print(f"your name is {name}")

#temperature = input("What is the temperature? ")
print(f"Tonight the temperature is {int(temperature) - 10} degrees")

#data conversion challenge
#celsius_temperature = input("What is the cuurent temperature in Celcius?")
#celsius_temperature = float(celsius_temperature)
#fahrenheit_temperature = celsius_temperature * 9 / 5 + 32
#print(f"It is currently {round(fahrenheit_temperature)} degrees Fahrenheit")

a = 'hello'
b = 'world'
print(a + " " + b)

a = 2
b = 'world'
#convert a into string to concatenate
print(str(a) + " " + b)
'''
This is a multi-line comment in Python 
'''

#Week 2 Python
sunny = False
rainy = True
#Logical operartors
print(a == b)
print(a != b)
print(10 > 5)
print(5 <= 6)  #etc

#Logical Operators
#and, or, not
print(a == 1 and b == 2)  #True
print(a == 2 and b == 2)  #False
print(a == 1 or b == 3)  #True
print(a == 4 or b == 0)  #False
print(not (a == 2))  #False

print(True and False and True and True)  #False
print(True and True and True and True)  #True
print(True or False or False or False)  #True
print(False or False or False or False)  #False

#Logical Operators Challenge Lesson 1 wk2
height = 170
age = 31
height != 160  #TRUE
height > 170 and age > 12  #False
height < 170 or age >= 12  #True
height >= 170 and age >= 31  #True
not (height >= 170 and age >= 31)  #False

age = input("What is your age? ")
age = int(age)

if age < 18:
    print(
        "You cannot vote"
    )  #No () needs to be indented and what inddented is what is run if the condition is met
    print(f"because you are {age} years old")
else:
    print("You can vote, you are old enough👌🏾")

age = input("How are old are you? ")
age = int(age)

if age >= 65 and age <= 90:
    print("You are wise")

if age < 18:
    print("You cannot vote")
    print(f"because you are {age} years old")
else:
    print("You're old enough to vote, congrats! 👏")

if age >= 21:
    print("You can party")
else:
    print("Stay home, you're too young to party")

#Homework Wk2 Lesson 3
temperature = input("What is the temp?")
temperature = int(temperature)

if temperature >= 20:
    print("Enjoy the sunshine")
else:
    print("Dont forget your jacket!👌🏾")

#Lesson 4
temperature = 20

if temperature > 30:
    print("Its warm")
elif temperature >= 20:
    print("It's a nice day")
elif temperature >= 10:
    print ("It's a bit cold") #elif is short for else if, you can have as many elif as you want
else:
    print("It's cold outside")

#Challenge Lesson 4
temperature = input("What is the temperature?")
temperature = int(temperature)

rainy = input("Is it raining? (yes/no)")
rainy = rainy.lower() #YES => yes, NO => no

if temperature > 20 and rainy == 'no':
    print("Enjoy your sunny day")
elif temperature >20 and rainy == 'yes':
    print("Dont forget your umbrella")
elif temperature < 20 and rainy == 'yes':
    print("Dont forget your umbrella and jacket")
else:
    print("Dont forget your jacket")

#none is a special value in Python that represents the absence of a value
city = None

if city:
    print(f"The city is {city}")
else:
    print("The city does not exist") #This will be printed because city is None



