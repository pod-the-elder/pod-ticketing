# Faux launcher for options
def printMenu():
    print(67 * "-")
    print("Mitch's Ticketing System")
    print("")
    print("1. Create a new ticket")
    print("2. Update an existing ticket")
    print("3. Read existing ticket")
    print("4. Close an existing ticket")
    print("5. Log work for open ticket")
    print(67 * "-")
loop=True

while loop:
    printMenu()
    choice = input ("Enter your choise [1-5]")

    if choice==1:
        print("Create a new ticket")
    elif choice==2:
        print("Update a ticket")
    elif choice==3:
        print("Read a ticket")
    elif choice==4:
        print("Close a ticket")
    elif choice==5:
        print("Log work for ticket")
        loop=False
    else:
        raw_input("Wrong option selected. Enter any key to try again...")
