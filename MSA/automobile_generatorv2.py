import automobile as auto
#Function load vehicle data from file
#Input: path to the file
#Output: list of automobiles
def load_vehicles(file_name):
    #Create an empty list to store automobile data
    list_of_automobiles = []
    #open the file
    auto_file = open(file_name, "r")

    #read each line of the file in a for loop
    for line_of_data in auto_file:

        #split each line at the comma to get values
        vehicle_data = line_of_data.split(",")

        #get individual values from the resulting list 
        print(vehicle_data)
        make = vehicle_data[0]
        model = vehicle_data[1]
        vin = vehicle_data[2]
        engine_size = float(vehicle_data[3])
        owner = vehicle_data[4]
        year = int(vehicle_data[5])
        #create automobile objects with the data
        new_auto = auto.Automobile(make, model, vin, engine_size, owner, year)
        #append eadch automobile to the list of automobiles
        list_of_automobiles.append(new_auto)

    auto_file.close()

    pass

def main():
    #load at list of automobiles from data in a file
    automobile_list = load_vehicles("vehicle_data.csv")
    pass

main()
