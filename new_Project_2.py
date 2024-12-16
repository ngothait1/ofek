entry = {}
def printMenu():                         
    print("1. Save a new entry ")
    print("2. search by ID ")
    print("3. Print ages average ")
    print("4. Print all names ")
    print("5. Print all IDs ")
    print("6. Print all entries ") 
    print("7. Print entry by index ")
    print("8. exit ")
    user_choice = input ("Please enter your choice: ")
    return user_choice

def digitisok(param):
    if param.isdigit():
        return True
    return False


def saveNewEntry(entry, avg):
    id = input("ID: ")
    if digitisok(id) == False:
        print("Error: " + id + " is not a number ")
        return -1
    name = input("Name: ")
    age = input("Age: ")
    if digitisok(age) == False:
        print("Error: " + age + "is not a number ")
        return -1    
    if id in entry:
        print("Error: ID " + id + "is alredy use. try again")
        return -1
    entry[id] = {"Name": name, "Age" : age}
    print("ID [" + id + "] saved successfuly ")
    print(entry)
    avg += int(age)
    return avg  
    
    
def searchById(entry):
    id_choice = input("Please Enter your ID you look for: ")
    if id_choice in entry:
        info = entry[id_choice]
        print("ID: " + id_choice)
        print("Name : " + info["Name"] )
        print("Age: " + info["Age"])
    else:
        print("Error: Id is wrong")
        return    
            

def printAgesAvarage(entry, avarage):
    if len(entry) != 0:
        print(avarage / len(entry))
    else:
        print("Error: Cant divide by zero")
        return
        

def printAllNames(entry):
    for index, id  in  enumerate(entry):
        print(str(index) + " . Name: " + entry[id]["Name"])

def printElegant(entry, it):
    for index, it in enumerate(entry):
            print(str(index) + ". " + "ID: " + it)
            print(str(index) + ". " + "Name: " + entry[it]["Name"])
            print(str(index) + ". " + "Age:"  + entry[it]["Age"])
   
def printAllIds(entry): 
    for index, id in enumerate(entry):
        print(str(index) + " Id: " +  id )

def printAllEntries(entry):
    printElegant(entry,id)

def printEntryByIndex(entry):
    choose_index = int(input("Please choose index: "))
    if int(choose_index) > len(entry) - 1:
        print("Error: index out of range ")
        return -1 
    else:
        key_list = list(entry.keys())
        print("Id: " + key_list[choose_index])
        item_list = list(entry.values())
        a_list = (list(item_list[choose_index].items()))
        print("Name: " + a_list[0][1])
        print("Age: " + a_list[1][1])


def main():
    avg = 0
    entry = {}
    while True:
        user_choice = printMenu()
        if user_choice == "1":
            temp = saveNewEntry(entry, avg)
            if temp != -1:
                avg = temp  
        elif user_choice == "2":
            searchById(entry)  
        elif user_choice == "3":
            printAgesAvarage(entry, avg) 
        elif user_choice == "4":
            printAllNames(entry)
        elif user_choice == "5":
            printAllIds(entry)
        elif user_choice == "6":
            printAllEntries(entry)                 
        elif user_choice == "7":
            printEntryByIndex(entry)
        elif user_choice == "8":
            exit_input = input("Are you sure? (y/n)")
            if exit_input == "n":
                return  
            else:
                print("Goodbye")
                break
        else:
            print("Eror: choose number between 1-8 and not something else...")        

main()             



    



