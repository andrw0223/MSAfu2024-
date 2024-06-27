def main():
    person1 = {"name": "Sam", "age": 17}
    person2 = {"name": "Frank", "age": 18}
    person3 = {"name": "Sam", "age": 16}
    person4 = {"name": "Cyd", "age": 17}

    #add person to a list
    person_list = []
    person_list.append(person1)
    person_list.append(person2)
    person_list.append(person3)
    person_list.append(person4)

    #write code that produces a list of unique names
    #output should be ["Sam", "Frank", "Cyd"]
    unique_names = []
    for name in person_list:
        if not(name["name"] in unique_names):
            unique_names.append(name["name"])

    print(unique_names)

main()