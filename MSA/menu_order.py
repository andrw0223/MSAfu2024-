#Funtion to load menu items from the fileand create a dictionary
#Input: none
#Output: dictionary of menu items
def get_menu_items():
    #create a file handle that gives us access to the file
    data_file = open("menu.txt", "r")
    #create an empty dictionary to store menu items and prices
    menu_items = {}

    #loop through data in the file and read the file one line at a time
    for line_of_data in data_file:
        #split the line of data at the comma using .split()
        keys_and_values = line_of_data.split(",")

        #get item and price from the resulting list and store in the dictionary
        item = keys_and_values[0]
        price = keys_and_values[1]
        menu_items[item] = price
    #close the file
    data_file.close

    return menu_items

def main():
    #
    menu = get_menu_items
    total_cost = 0
    while(True): 
            order_item = input("\nItem: \n")
            if (order_item in menu):
                total_cost = total_cost + menu[order_item]
                print(f"Total: ${total_cost:.2f}")
                continue
            elif (order_item.lower() == 'end' ):
                break
            else:
                continue

main()



#menu.txt:
#Baja Taco,4.00
#Burrito,7.50
#Bowl,8.50
#Nachos,11.00
#Quesadilla,8.50
#Super Burrito,8.50
#Super Quesadilla,9.50
#Taco,3.00
#Tortilla Salad,8.00

  
