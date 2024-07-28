#Naming the function read from a 'stock.txt' file and return a dictionary
def read():
    try:
        with open('stock.txt', 'r') as file:
            ca = {} #Initialize an empty dictionary to store equipment data
            for line_num, line in enumerate(file, start=1):
                line = line.strip()  # remove leading/trailing whitespace
                if not line:  # skip empty lines
                    continue
                parts = line.split(', ')
                if len(parts) != 4:  # skip lines with invalid format
                    print(f"Skipping line {line_num}: invalid format ({line})")
                    continue
                ca[line_num] = parts #Store equipment data into a dictionary
    except FileNotFoundError:
        print("stock.txt not found")
        #Return an empty dictionary if file not found
        ca = {}
    return ca #Return the dictionary of equipment data
#Creating a function tab to determine the amount of tab chaaracters based on the string length
def tab(str_val):
    """Returns tab characters based on the length of the given string"""
    if len(str_val) <= 8:
        return "\t\t"
    else:
        return "\t"

#function to display a formatted table of equipment data
def table(equipment_data):
    """Displays a formatted table of equipment data"""
    print(
        "--------------------------------------------------------------------------------------------------")
    print("S/N. \tName \t\t\t Brand Name  \t\tPrice \t\tQuantity")
    print(
        "--------------------------------------------------------------------------------------------------")

    # Loop through each equipment in the equipment_data dictionary
    for key, values in equipment_data.items():
        #printing the formatted equipment information
        print(f"{key}.     {values[0]} \t\t {values[1]} \t\t {values[2]} \t\t {values[3]}")
        print(
            "----------------------------------------------------------------------------------------------")
