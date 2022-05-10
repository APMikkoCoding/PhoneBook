from tinydb import TinyDB, Query

# Makes Database
db = TinyDB("phonebook.json")
user = Query()

# Clears Terminal
print(chr(27) + "[2J")

class PhoneBook:
    # This adds a person
    def addPerson(name, number):
        db.insert({"name": name, "number": number})

    # This finds a person
    def findPerson(option):
        if db.search(user.name == option) != None:
            name = db.search(user.name == option)
            name = name[0]
            return name["name"], name["number"]
            
        elif db.search(user.number == option) != None:
            number = db.search(user.number == option)
            return number["name"], number["number"]
            
    # This lists all people
    def allPeople():
        for i in range(len(db)):
            names = db.search(user.name != None)
            person = names[i]
            name = person["name"]
            number = person["number"]
            print(f"Person {i+1}",f"Name ---> {name}, Number ---> {number}")
            

print("Welcome to PhoneBook by APMikko Coding")

while True:

    # Print Users Options
    print("1. Add Person\n2. Find Person\n3. Find All People")
    thing = int(input("Operation (1/2/3) : "))
    print(chr(27) + "[2J")

    # Adds Person
    if thing == 1:
        name = input("Name of Person: ")
        number = int(input("Number of Person EXP. (3334445555): "))
        if number > 1000000000 and number < 9999999999:
            PhoneBook.addPerson(name, number)
        else:
            print("Not added")
    
    # Finds Person
    elif thing == 2:
        option = input("Input name or number: ")
        name, number = PhoneBook.findPerson(option)
        print(f"Name of Person ---> {name}, Number of Person ---> {number}")

    elif thing == 3:
        PhoneBook.allPeople()

    # Continue Function
    con = input("Continue(y/n): ").lower()

    if con == "n":
        break

    # Clears Terminal
    print(chr(27) + "[2J")