#August Harris
#2/19
#Initialize

groccerylist = ["Cheese", "Bacon", "Kiwi", "Strawberrys", "Bread", "Soap"]

#Functions
#Adds an item to the list
def add():    
    add= input("What do vou want to add to the list?: ")
    groccerylist.append(add)
    print(groccerylist)
    shoppinglist2()

#Lets the user view the list
def view():
    print(groccerylist)
    shoppinglist2()

#Marks specific things as completed
def complete():
    the = (input("What item would you like marked completed? "))
    groccerylist.replace(the, "x")
    print(groccerylist)

    shoppinglist2()

#Removes items from the list
def remove():
    remove= input("What do vou want to remove from the list?: ")
    groccerylist.remove(remove)
    print(groccerylist)
    shoppinglist2()

#Exits the groccery list
def exit():
    exit = input("Do you want to exit the shopping list?: ")
    if exit == "Yes":
        print("You are exiting the shopping list.")
    else:
        shoppinglist()
    shoppinglist2()
#Removes all the tasks from the list
def removeall():
    groccerylist.clear()
    print(groccerylist)
    shoppinglist2()
#Sorts the list alphabetically
def sortlist():
    groccerylist.sort()
    print(groccerylist)
    shoppinglist2()
#Counts the number of items in the list
def itemslist():
    x = len(groccerylist)
    print(x)
    shoppinglist2()

# Lets the user use the functions above on their groccery lsit  
def shoppinglist():
    print("Here is your shopping list.")
    print("Please select an option.")
    option = int(input("Option: "))
    if option == 1:
        add()
    if option == 2:
        view()
    if option == 3:
        complete()
    if option == 4:
        remove()
    if option == 5:
        exit()
    if option == 6:
        removeall()
    if option == 7:
        sortlist()
    if option == 8:
        itemslist()
def shoppinglist2():
    print("Please select an option.")
    option = int(input("Option: "))
    if option == 1:
        add()
    if option == 2:
        view()
    if option == 3:
        complete()
    if option == 4:
        remove()
    if option == 5:
        exit()
    if option == 6:
        removeall()
    if option == 7:
        sortlist()
    if option == 8:
        itemslist()

#Main
shoppinglist()
