def main():
    #Capitalize a string
    my_name = "andrew"
    print(my_name.capitalize())

    #Make a string uppercase
    print(my_name.upper())

    #Make a string lowercase
    last_name = "FU"
    print(f"{my_name.capitalize() }{last_name.lower()}")
    
    #Determine if a string starts with a set of characters
    print(my_name.startswith("a"))

    if(not my_name.startswith("andr") and not my_name.startswith("Andr")):
       print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    #Determine if a string ends with a specified set of characters
    print(my_name.endswith("rew"))

    #find a set of characters in a string
    print(my_name.find("w", 5))

    #loop through a string
    print("\n\n")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters")

    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index: {my_name[letter_index]}}")

    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #write code that counts the number of occurences of dog in the sentence
    #expected output: 3
    #use a while loop to read the string
    #start at the beginning of the string
    #read the string until you find the first occurence of dog
    #add 1 to the number of found dogs
    #continue reading from the next index: update the start index in the find method

    index_number = 0
    number_dog = 0
    while (not index_number == -1 ):
        index_number = sentence.find("dog", index_number + 1)
        number_dog += 1


    print(number_dog - 1)
main()
