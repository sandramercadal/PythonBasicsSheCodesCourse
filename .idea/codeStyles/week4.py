#week4 Dictionaries e.g to hold JSON objects like an object in JS

#create a dictionary with key value pairs
temperatures = {
    "Lisbon": 12,
    "Paris": 6,
    "Madrid": 15,
    "Berlin": 4
}
#the above can also be on one line but it reads better on multiple lines

dictionaries = {"people": "definition of people", "Python": "definition of Python"}

#accessing the dictionary
print(temperatures) #{'Lisbon': 12, 'Paris': 6}
print(temperatures["Lisbon"]) #12
#This will crash as value not there >> print(temperatures["New York"])

#accessing the dictionary with get
print(temperatures.get("Lisbon")) #12
print(temperatures.get("New York")) #None

#creating an empty dictionary
winners ={}
print(winners) #{} prints an empty dictionary

#accessing values
ranking = {1: "Sara", 2: "Julie", 3: "Jen", 3: "Liz"}

#modifying values and updating them. Lisbon is already in the dictionary so it will update it, it was 12 now it is 15
temperatures["Lisbon"] = 15
print(temperatures["Lisbon"]) #15

#Removing a ket value pair
del temperatures["Lisbon"]
print(temperatures) #Lisbon is now gone {'Paris': 6}, Madrid and Berlin is left

temperatures.pop("Paris") #removes Lisbon from the dictionary
print(temperatures)
temperatures.popitem() #removes the last item in the dictionary so Berlin is gone

#A dictionary with dictionaries inside it
students = {
    "Alice": {"id": "ID0001",
              "age": 26,
              "grade": "A",
              "graduated": True},
    "Bob": {"id": "ID0002",
            "age": 27,
            "grade": "B"},
    "Claire": {"id": "ID0003",
               "age": 17,
               "grade": "C"},
    "Dan": {"id": "ID0004",
            "age": 21,
            "grade": "D"},
    "Emma": {"id": "ID0005",
             "age": 22,
             "grade": "E"}
}
print(students)
print(students["Alice"])

#week4 homework
#1)create a dictionary of 3 countries with their capitals as key value pairs.
#2) Print the dictionary
#3) Remove the least fav and print
#4) Add another country and print
#5) Display the capital of each country (one at a time, don't use a loop)

