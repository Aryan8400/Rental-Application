import read
import write
import datetime
import math
import os

# Function to round up a number to the nearest multiple of 5
def round_up_to_nearest_multiple_of_5(number):
    return math.ceil(number / 5) * 5

# Function to handle the process of returning  assets
def Return(ca):
    running = True
    assets = [] #list to stored return assets and quantities

    # Ask for Returner's name
    print("")
    run = True
    while run:
        rentor_name = input("Enter the name of the Returner: ").lower()#get the returner name in lower case to avoid case-sensitive
        directory_path = os.path.dirname(os.path.abspath(__file__))#get the absolute path of the file
        file_extension = ".txt"

        file_to_search = rentor_name + file_extension#generate a file name to search
        file_path = os.path.join(directory_path, file_to_search)#create a path to the file
        #giving a condition to check whether the returner name has rented from this store or not 
        if os.path.exists(file_path):
            print("Old Customer .")
            run = False
        else:
            print("User not found.")
            run = True

    # loop(running) to keep extra assets until user chooses to stop
    while running == True:
        print("")
        print("Showing you our list of Equipments ...")
        read.table(ca)
        print("")

        # Get the equipment option from user
        while running == True:
            try:
                dicision_user = int(input("Enter the option of the Equipment you want to Return: "))

                if dicision_user <= 0 or dicision_user > len(ca):
                    print("")
                    print("Invalid input! Kindly try again!")
                    print("")
                    continue
                else:
                    break
            except:
                print("")
                print("An error has occured! Kindly try again!")
                print("")
        print("")

        # Get the quantity of the equipment to return from user
        while running == True:
            try:
                selected_quantity = int(input("Enter the quantity of the Equipment that you want to Return "))
                if selected_quantity <= 0:
                    print("")
                    print("Sorry the selected quantity is not avaliable in our shop!")
                    print("")
                    continue
                else:
                    break
            except:
                print("")
                print("An error has occured! Kindly try again!")
                print("")
        print("")
        # add the equipment and quantity to the list of returned equipment
        assets.append([dicision_user, selected_quantity])
        # Update the stock quantity of the returned equipment in the product dictionary
        ca[dicision_user][3] = str(int(ca[dicision_user][3]) + selected_quantity)

        # Ask if user wants to return more equipments
        extra = input("Do You Want to Return More Equipments? y/n: ").lower()
        if extra == "y":
            continue
        else:
            break

    a = 1
    totalamt = 0

    # Write the updated stock quantity to the equipment file
    print("")
    print("Kindly wait while we generate your bill...\n")
    print(
        "--------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\tAryan Rental Shop")
    print("\t\t\t\t\t\tKathmandu,Nepal")
    print("\t\t\t\t\t\tReturn Date: " + str(datetime.date.today()))
    print(
        "--------------------------------------------------------------------------------------------------")
    print("")
    print("Returner: " + rentor_name)
    print("")
    print(
        "---------------------------------------------------------------------------------------------------")
    print("S/N\tName\t\tBrand\t\tQuantity\tUnit Price\tNet Price")
    print(
        "----------------------------------------------------------------------------------------------------")
    # Iterate over the list of returned assets to generate the invoice
    for i in assets:
        index = i[0]
        # Calculate the net price of the equipments
        overall_price = int(ca[index][2].replace("$", "")) * int(i[1])
        # Display the returned equipments details in the invoice
        print(
            str(a) + "\t" + ca[index][0] + read.tab(ca[index][0]) + ca[index][1] + read.tab(ca[index][1]) + "   " + str(
                i[1]) + "\t\t  " + ca[index][2] + "\t\t$" + str(overall_price))
        a += 1
        totalamt += overall_price
    valid = True
    while valid:
        valid_charge = int(input("\nFor how many days Did the Costumer Rented the Equipment?: "))
        daysbasis = round_up_to_nearest_multiple_of_5(valid_charge)
        currentamt = (daysbasis / 5) - 1
        Extra_Charge = 0
        if valid_charge > daysbasis:
            Extra_Charge = currentamt * totalamt
            valid = False
        elif valid_charge <= 0:
            print("Not valid amount of days please try again")
            valid = True
        else:
            Extra_Charge = currentamt * totalamt
            valid = False
    # Display the total amount and gross amount with the Extra Charge in the invoice
    print(
        "----------------------------------------------------------------------------------------")
    print("Net Amount: $" + str(totalamt))
    print("Gross Amount: $" + str(totalamt))
    if Extra_Charge != 0:
        print("5 Days Exceeded: $" + str(Extra_Charge))
        print("Every 5 days after first 5 days: ", totalamt)
    print("Total Amount: $" + str(totalamt + Extra_Charge))
    write.write(ca)
    write.invoice_for(ca, assets, rentor_name, Extra_Charge)

#Function for renting the equipments
def rent(ca):
    # Initialize variables and list
    running = True
    assets = []
    print("")

    # Get customer's name and contact number
    run = True
    while run:
        name_of_user = input("Enter the name of the customer: ")
        if name_of_user.isalpha() == True:
            run = False
        else:
            print("Invalid Name")
            run = True
    while running == True:
        try:
            user_num = int(input("Enter the contact number of the customer: "))
            # Break out of running once user enters a valid integer
            break
        except:
            print("")
            print("An error occured! Kindly try again!")
            print("")
    print("")

    # Select equipment to rent  and get quantity for each
    while running == True:
        print("")
        print("Showing you the list of Equipments That are for Rent...")
        read.table(ca)
        print("")

        # Select equipment to rent and get quantity for each
        while running == True:
            try:
                dicision_user = int(input("Enter the option of the Equipments to Rent: "))
                if dicision_user <= 0 or dicision_user > len(ca):
                    print("")
                    print("Invalid input! Please try again!")
                    print("")
                    continue
                else:
                    break
            except:
                print("")
                print("An error has occured! Kindly try again!")
                print("")
        print("")

        # running until user enters a valid integer option
        while running == True:
            try:
                selected_quantity = int(input("Enter the quantity of the Equipments to Rent: "))
                if selected_quantity <= 0 or selected_quantity > int(ca[dicision_user][3]):
                    print("")
                    print("Not a valid input! Kindly Please try again!")
                    print("")
                    continue
                else:
                    break
            except:
                print("")
                print("Not a valid input!Kindly try again!")
                print("")
        print("")
        days = int(input("For how many days you want to rent the equipment: "))
        # extra selected equipment and quantity to list
        assets.append([dicision_user, selected_quantity])
        # Update inventory quantity
        ca[dicision_user][3] = str(int(ca[dicision_user][3]) - selected_quantity)

        # Ask if user wants to rent extra more Equipments
        extra = input("Are you interested in Renting more Equipments? y/n ").lower()
        if extra == "y":
            continue
        else:
            break
    # Ask if user wants to add more Equipments
    a = 1
    totalamt = 0

    # Write updated equipment to file
    write.write(ca)
    print("")
    # Generate and display rented invoice
    print("Kindly wait for a moment while we generate your invoice...\n")
    print(
        "----------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t Aryan Rental Shop")
    print("\t\t\t\t\t\t Kathmandu, Nepal")
    print("\t\t\t\t\t\t Purchase Date: " + str(datetime.date.today()))
    print(
        "----------------------------------------------------------------------------------------------------")
    print("")
    print("Name of the Customer Name: " + name_of_user)
    print("Contact Number of the customer: " + str(user_num))
    print("")
    print(
        "----------------------------------------------------------------------------------------------------")
    print("S/N\tName\t\tBrand\t\tQuantity\tUnit Price\tNet Price")
    print(
        "----------------------------------------------------------------------------------------------------")
    # Iterate over the list of rented assets to generate the invoice
    for i in assets:
        index = i[0]
        overall_price = int(ca[index][2].replace("$", "")) * int(i[1])
        print(
            str(a) + "\t" + ca[index][0] + read.tab(ca[index][0]) + ca[index][1] + read.tab(ca[index][1]) + "   " + str(
                i[1]) + "\t\t  " + ca[index][2] + "\t\t$" + str(overall_price))
        a += 1
        totalamt += overall_price

    print(
        "--------------------------------------------------------------------------------------------------")
    print("Net Amount: $" + str(totalamt))
    write.bill_s(ca, assets, name_of_user, user_num)
