city = input("What city are you currently in? ")
temperature = input(
    f"What's the temperature today in your {city} in Celsius? ")
#temperature = int(temperature)

if not city and not temperature:
    print("You did not enter a city or temperature")

else:
    temperature = int(temperature)

    if temperature > 20:
        print(
            f"It is currently warm in {city} with a temperature of {temperature}ºC"
        )
    elif temperature >= 10 and temperature < 20:
        print(
            f"It is currently chilly in {city} with a temperature of {temperature}ºC"
        )
    else:
        print(
            f"It is currently cold in {city} with a temperature of {temperature}ºC"
        )

#Wk3 Lesson 4

students = ["John", "Jane", "Sarah", "Sandra", "Sam"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
certificate = []

print(students[0])  # prints John
print(students[1])  # prints Jane
print(len(students))  # prints 5 as there are five students in the list
#Update an element in a list
students[0] = "Jake"  # replaces John with Jake
print(students)
students.append("Sofia")
print(students)
students.insert(3, "Matilde")
print(students)
students.remove("Sandra")
print(students)
students.pop()  # removes the last element in the list
print(students)
students.pop(2)  # removes the element at index 2
del students[0]  # deletes the element at index 0

#order a list
students = ["John", "Jane", "Sarah", "Sandra", "Sam"]
students.sort()
print(students)  # prints ['Jane', 'John', 'Sam', 'Sarah', 'Sandra']

#Challenge 1 week 3 - create a list of 3 countries print the list
#b) remove the last country, Print out the list,
#c)Add another element at the beginning of the list, Print out the list, #d) Print out the length of the list,
#e)Sort the list , Print out the list
countries = ["Trinidad", "Norway", "Japan"]
print(countries)  #=> ['Trinidad', 'Norway', 'Japan']
#b) remove the last country
countries.pop()  #=> ['Trinidad', 'Norway']
print(countries)
#c) add a country at the beginning of the list
countries.insert(0, "Spain")  #=> ['Spain', 'Trinidad', 'Norway']
print(countries)
#d) print last element of the list
print(countries[-1])  #=> Norway
#d) print the length of the list
print(len(countries))
print(f"The length of the list is {len(countries)}"
      )  #=> The length of the list is 3
#e) sort the list
countries.sort
print(countries)  #=> ['Norway', 'Spain', 'Trinidad']

#remove an element of the list
students.remove("Sandra")
print(students)
students.pop(2)
print(students)
# not very elegant is del
del students[0]
#order a list
students = ["John", "Jane", "Sarah", "Sandra", "Sam"]
students.sort()
print(students)  #=> ['Jane', 'John', 'Sam', 'Sarah', 'Sandra']
print(sorted(students))  #doesnt override original list
students.reverse()
print(students)

#For-Loop
students = ["John", "Jane", "Sarah", "Sandra", "Sam"]
for student in students:
    print(student)
    print(f"The students name is {student.title()}")
#things are executed depening on the indentation

threeCountries = ["Costa Rica", "Seoul", "Tokyo"]
#Loop through each country and print out the following sentence with the correct country and the correct number My number 1 country is Canada,My number 2 country is Brazil,My number 3 country is Japan

moreCountries = ["Canada", "Brazil", "Japan"]
index = 0
for country in moreCountries:
    print(f"My number {index+1} country is {country}")
    index = index + 1
    #My number 1 country is Canada,My number 2 country is Brazil,My number 3 country is Japan
