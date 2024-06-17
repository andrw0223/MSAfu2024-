def main():
#list [1, 4, 6, 7, 78]
    scores = [1,4,6,7,78]
    student_names = ["Alice", "Bob", "Jerry", "Jane", "Bill"]
    for index in range(len(scores)):
        print(f"{student_names[index]}: {scores[index]}")

    #Create a dictionary of names and scores
    student_scores = {
        "Alice": 87,
        "Bob": 79,
        "Jerry": 94,
        "Sara": 90
    }
    #print Bob and Sara's socres
    print(student_scores["Bob"])
    print(student_scores["Sara"])

    #get all the keys and values form the student score dictionary
    print("\n\n")
    for student in student_scores: 
        print(f"{student}: {student_scores[student]}")
    
    #Declare a car dictionary
    car = {"Make": "Ferrarri", "Model": "F-50", "Year": 2021, "Value": 500000, "Engine": 4.8}

    #Get all the keys and and values from the car dictionary
    print("\n\n")
    for key, value in car.items():
        print(f"{key}: {value}")
main()
