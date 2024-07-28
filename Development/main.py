"""
Aryan Rental Shop
This code implements a basic rental shop management system.User can view
available equipment,rent and return the equipments and exit the program
"""
#import the required modules for reading the data and performing the operation
import read,operation
#import datetime to work with date and times
from datetime import datetime

#get the current date and time 
now = datetime.now()

current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")
print(" ")
#Displaying date and time
print("\t\t\t\t\t\t\t\t",current_date)
print("\t\t\t\t\t\t\t\t",current_time)

# Welcome message
print("\n \t \t \t Welcome to Aryan Rental Shop!")
print("----------------------------------------------------------------------------------")
print(" \t \t We offer a wide selection of equipment at affordable prices.")
print("----------------------------------------------------------------------------------")
print("Please select an option from the menu below:")
print("----------------------------------------------------------------------------------")

# Main loop to keep program running
running = True
while running:
    # Read in the list of assets
    assets = read.read()

    # Display the menu options
    print("\nMenu Options:")
    print("----------------------------------------------------------------------------------")
    print("1. View available Equipment to Rent")
    print("2. Rent an Equipment")
    print("3. Return an Equipment")
    print("4. Exit")
    print("----------------------------------------------------------------------------------")

    # Get the user's choice and handle invalid inputs
    while True:
        try:
            option = int(input("\nEnter your choice: "))
            if option < 1 or option > 4:
                print("Invalid input. Please enter a number between 1 and 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    # Execute the chosen option
    if option == 1:
        print("\nPresenting you our top quality Equipments for Rent ")
        read.table(assets)
    elif option == 2:
        operation.rent(assets)
    elif option == 3:
        operation.Return(assets)
    elif option == 4:
        print("\nThank you for visiting Aryan Rental Shop!")
        print("Feel free to contact us in our telephone number +02378946787 for any queries")
        running = False #Exit the loop and terminate the program
    else:
        print("\nInvalid input. Kindly try again.")
