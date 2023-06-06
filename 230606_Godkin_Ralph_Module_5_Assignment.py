
import random

# IMPORT SYS TO ACCESS PROGRAM EXIT FUNCTIONALITY ###########################
import sys  
 
ITEMS_FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"
 
def read_items():
    items = []
# ERROR HANDLING TO TEST IF FILE EXISTS #####################################
    try: 
        with open(ITEMS_FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                items.append(line)
        return items
# IF ALL ITEMS FILE NOT FOUND EXIT THE PROGRAM GRACEFULLY ###################
    except FileNotFoundError as fe:
        print('\nOh no! All items have disappeared! We\'re gonna have to get to the bottom of this.\n')
        print('What we know: ', fe)
        sys.exit('\n >>>  Game has terminated  <<< \n')

def read_inventory():    
    inventory = []
# ERROR HANDLING TO TEST IF FILE EXISTS ####################################
    try: 
        with open(INVENTORY_FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                inventory.append(line)
# IF WIZARD INVENTORY FILE NOT FOUND, DISPLAY MESSAGE AND CREATE THE FILE ##
    except FileNotFoundError as fe:
            print('Could not find inventory file. \nWizard is starting with no inventory.')
            with open(INVENTORY_FILENAME, "w"):
                print('Inventory file created.\n')
    return inventory
 
def write_inventory(inventory):
    with open(INVENTORY_FILENAME, "w") as file:
        for item in inventory:
            file.write(item + "\n")
 
def display_title():
    print("The Wizard Inventory program")
    print()    
 
def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()
 
def walk(inventory):
    items = read_items()
    item = random.choice(items)
    print("While walking down a path, you see " + item + ".")
    choice = input("Do you want to grab it? (y/n): ")
    if choice == "y":
# ERROR HANDLING TO TEST IF INVENTORY EXISTS #########################################
        try:
            if len(inventory) >= 4:
                print("You can't carry any more items. " + 
                    "Drop something first.\n")
            else:
                inventory.append(item)
                print("You picked up " + item + ".\n")
                write_inventory(inventory)
    # IF THERE IS NO INVENTORY PICK UP THE ITEM WITHOUT CHECKING THE ITEM COUNT ######
        except TypeError as te:
                print('')
                inventory.append(item)
                print("You picked up " + item + ".\n")
                write_inventory(inventory)
    else:
        print()
 
def show(inventory):
# CHECK IF THERE IS INVENTORY TO SHOW, OR NOT #######################################
    if inventory == []:
        print('You don\'t have any inventory yet.\n')
    else:
        for i in range(len(inventory)):
            item = inventory[i]
            number = i + 1
            print(str(number) + ". " + item)
        print()
 
def drop_item(inventory):
# CHECK IF THERE IS INVENTORY TO SHOW, OR NOT ######################################
    if inventory == []:
        print('You don\'t have any inventory to drop.\n')
    else:
# ERROR HANDLING THE DROP INVENTORY INPUT ##########################################
        try:
            number = int(input("Number: "))
            if number < 1 or number > len(inventory):
                print("Invalid item number.\n")
            else:
                item = inventory.pop(number-1)
                print("You dropped " + item + ".\n")
                write_inventory(inventory)
        except ValueError as e:
            print("Please use an integer. Try again.\nError: ", e, "\n")
    
def main():
    display_title()
    display_menu()
 
    inventory = read_inventory()
    while True:        
        command = input("Command: ")        
        if command == "walk":
            walk(inventory)
        elif command == "show":
            show(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
 
if __name__ == "__main__":
    main()