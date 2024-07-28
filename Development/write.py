import read, datetime
# Function to get the current date and time as a string
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    return year + "_" + month + "_" + day

# Function to write the equipment data to a file
def write(ca):
    file = open('stock.txt', 'w')
    for i in ca.values():
        file.write(", ".join(i) + "\n")
    file.close()
    
# Function to generate a returning invoice
def invoice_for(ca, assets, customer_name,Extra_Charge):
    # Generate the filename for the invoice based on the Customer name and current date and time
    filename = customer_name +".txt"
    file = open(filename, "w")
    # Write the header information to the file
    file.write("Return Bill\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\t\tAryan Rental Shop\n")
    file.write("\t\t\t\t\t\tKathmandu, Nepal\n")
    file.write("\t\t\t\t\t\tReturn Date: " + str(datetime.date.today()) + "\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Customer: " + customer_name.lower() + "\n")
    file.write("\n")
    # Write the table header to the file
    file.write(
        "------------------------------------------------------------------------------------------------------------------------\n")
    file.write("S/N \tName \t\t Brand \t\tQuantity \t Unit Price\t Net Price\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------------------\n")
    a = 1
    totalamt = 0
    # Loop through each item in the assets list and write the equipment information to the file
    for i in assets:
        index = i[0]
        overall_price = int(ca[index][2].replace("$", "")) * int(i[1])
        file.write(str(a) + read.tab(ca[index][0]) + ca[index][0] + read.tab(ca[index][0]) + ca[index][1] + read.tab(
            ca[index][1]) + "   " + str(i[1]) + "\t\t  " + ca[index][2] + "\t\t $" + str(overall_price) + "\n")
        a += 1
        totalamt += overall_price
    # Write the footer information to the file
    file.write(
        "---------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("Net Amount: $" + str(totalamt) + "\n")
    if Extra_Charge!=0:
        file.write("Extra Charge: $" + str(Extra_Charge) + "\n")
        file.write("Total Amount: $" + str(totalamt + Extra_Charge) + "\n")
    else:
        file.write("Total Amount: $" + str(totalamt) + "\n")
    file.close()


# Function to generate a rent invoice
def bill_s(ca, assets, name_of_user, user_num):
    # Generate the filename for the invoice based on the customer name and current date and time
    filename = name_of_user +".txt"
    file = open(filename, "w")
    # Write the header information to the file
    file.write("Rent Bill\n")
    file.write(
        "---------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\t\tAryan Rental Shop\n")
    file.write("\t\t\t\t\t\tKathmandu, Nepal\n")
    file.write("\t\t\t\t\t\tPurchase Date: " + str(datetime.date.today()) + "\n")
    file.write(
        "---------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Customer Name: " + name_of_user.lower() + "\n")
    file.write("Contact Number: " + str(user_num) + "\n")
    file.write("\n")
    file.write(
        "---------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("S/N\t Name\t\tBrand\t\tQuantity\tUnit Price\tNet Price\n")
    file.write(
        "---------------------------------------------------------------------------------------------------------------------------------------------\n")
    a = 1
    totalamt = 0
    for i in assets:
        index = i[0]
        overall_price = int(ca[index][2].replace("$", "")) * int(i[1])
        file.write(str(a) + read.tab(ca[index][0]) + ca[index][0] + read.tab(ca[index][0]) + ca[index][1] + read.tab(
            ca[index][1]) + "   " + str(i[1]) + "\t\t  " + ca[index][2] + "\t\t $" + str(overall_price) + "\n")
        a += 1
        totalamt += overall_price
    file.write(
        "---------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("Net Amount: $" + str(totalamt) + "\n")
    
