#Create a program that accepts a hwy number and outputs the direction
#User enter: 95 
#Output: Interstate 95 runs South to North

def main():
    while(True):
        try: 
            highway_number = int(input("Enter a highway number(integer): "))
            if (highway_number < 1):
                print("ERROR: Please enter a positive integer")
                continue
            elif (highway_number % 2 == 1):
                print(f"Highway number {highway_number} runs North to South ")
                break
            else:
                print(f"Highway number {highway_number} runs East to West")
                break
        except:
            print("ERROR: Please enter an integer")
            continue


main()
