#write 2 functions that get the level and number of questions from the user
#Based on the answers write a for loop and random functions to print the desired number of questions
#Use error handling in the problems
import random
def get_level():
    while(True):
        level_number = input("Enter Level 1, 2, 3: ")
        if(level_number in ['1', '2', '3']):
            return level_number
        else:
            print("Error: Invalid input!")
            continue

def get_number_of_questions():
    while(True):
        question_number = input("Enter number of questions to ask: 3 to 10: ")
        if (question_number in ['3', '4', '5', '6', '7', '8', '9', '10']):
            return question_number
        else:
            print("ERROR: Please enter an integer value between 3 and 10!")

def main():
    user_level =  int(get_level())
    user_number_of_questions = int(get_number_of_questions())

    #Write an if loop for each level
    if(user_level == 1):
        #write for loops for each level
        for i in range (user_number_of_questions):
            a = random.randint(0,9)
            b = random.randint(0,9)
            counter = 0
            while(True):
                answer = int(input(f"{a} + {b} = "))
                if(answer == a + b):
                    print("CORRECT!!!")
                    break
                else:
                    print("WRONG!!!")
                    counter += 1
                    if (counter == 3):
                        print(f"Correct Answer: {a} + {b} = {a + b}")
                        break

    #if(user_level = 2):

    #if(user_level = 3):

main()
