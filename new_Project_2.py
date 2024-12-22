users_dict = {}
users_list = []
def printMenu():                         
    print("1. Save a new Entry ")
    print("2. search by ID ")
    print("3. Print ages average ")
    print("4. Print all names ")
    print("5. Print all IDs ")
    print("6. Print all entries ") 
    print("7. Print users_dict by index ")
    print("8. exit ")
    user_choice = input ("Please enter your choice: ")
    return user_choice

def digitisok(param):
    if param.isdigit():
        return True
    else:
        print("Error: " + param + " is not a number ")
        return  False
       
        


def saveNewEntry(users_dict, users_list, sum):
    id = input("ID: ")
    if digitisok(id) == False:
       # print("Error: " + id + " is not a number ")
        return -1
    name = input("Name: ")
    age = input("Age: ")
    if digitisok(age) == False:
       # print("Error: " + age + "is not a number ")
        return -1    
    if id in users_dict:
        print("Error: ID " + id + "is alredy use. try again")
        return -1
    users_dict[id] = {"Name": name, "Age" : age}
    users_list.append(id)
    users_list.append(name)
    users_list.append(age)
    print(users_list)
    print("ID [" + id + "] saved successfuly ")
    print(users_dict)
    sum += int(age)
    return sum  
    
    
def searchById(users_dict):
    id_choice = input("Please Enter your ID you look for: ")
    if id_choice in users_dict:
        info = users_dict[id_choice]
        print("ID: " + id_choice)
        print("Name : " + info["Name"] )
        print("Age: " + info["Age"])
    else:
        print("Error: Id is wrong")
        return    
            

def printAgesAvarage(users_dict, avarage):
    if len(users_dict) != 0:
        print(avarage / len(users_dict))
    else:
        print("Error: Cant divide by zero")
        return
        

def printAllNames(users_dict):
    for index, id  in  enumerate(users_dict):
        print(str(index) + " . Name: " + users_dict[id]["Name"])

# def printElegant(users_dict, id):
#     for index, id in enumerate(users_dict):
#         print(str(index) + ". " + "ID: " + id)
#         print(str(index) + ". " + "Name: " + users_dict[id]["Name"])
#         print(str(index) + ". " + "Age:"  + users_dict[id]["Age"])

def printAllIds(users_dict): 
    for index, id in enumerate(users_dict):
        print(str(index) + " Id: " +  id )

def printAllEntries(users_dict):
    for index, id in enumerate(users_dict):
        print(str(index) + ". " + "ID: " + id)
        print(str(index) + ". " + "Name: " + users_dict[id]["Name"])
        print(str(index) + ". " + "Age:"  + users_dict[id]["Age"])


#def printusers_dictByIndex(users_dict):

    # choose_index = int(input("Please choose index: "))
    # if int(choose_index) > len(users_dict) - 1:
    #     print("Error: index out of range ")
    #     return -1 
    # else:
    #     key_list = list(users_dict.keys())
    #     print("Id: " + key_list[choose_index])
    #     item_list = list(users_dict.values())
    #     a_list = (list(item_list[choose_index].items()))
    #     print("Name: " + a_list[0][1])
    #     print("Age: " + a_list[1][1])

def printusers_dictByIndex(users_list):
    choose_index = int(input("Please Choose index: "))
    if choose_index > len(users_list) - 3:
        print("Error: index out of range ")  
        return -1
    else:
        i = choose_index * 3
        print("Id : " + users_list[i]) 
        print("Name : " + users_list[i + 1])
        print("Age : " + users_list[i + 2])




def main():
    sum = 0
    users_dict = {}
    printMenu()
    while True:
        continue_input = input("Press Enter to continue: ")
        user_choice = printMenu()
        if user_choice == "1":
            temp = saveNewEntry(users_dict,users_list, sum)
            if temp != -1:
                sum = temp  
        elif user_choice == "2":
            searchById(users_dict)  
        elif user_choice == "3":
            printAgesAvarage(users_dict, sum) 
        elif user_choice == "4":
            printAllNames(users_dict)
        elif user_choice == "5":
            printAllIds(users_dict)
        elif user_choice == "6":
            printAllEntries(users_dict)                 
        elif user_choice == "7":
            printusers_dictByIndex(users_list)
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



    



