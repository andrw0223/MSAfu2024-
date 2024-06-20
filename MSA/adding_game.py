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
def run_game(level):
    if(level == 1):
        a = random.randint(0,9)
        b = random.randint(0,9)
    if(level == 2):
        a = random.randint(10,99)
        b = random.randint(10,99)
    if(level == 3):
        a = random.randint(100,999)
        b = random.randint(100,999)
    counter = 0
    while(True):
        try:
            answer = int(input(f"{a} + {b} = "))
            if(answer == a + b):
                print("CORRECT!!!")
                return True
            else:
                print("WRONG!!!")
                counter += 1
                if (counter == 3):
                    print(f"Correct Answer: {a} + {b} = {a + b}")
                    return False
        except:
            print("WRONG!!!")
            counter += 1
            if (counter == 3):
                print(f"Correct Answer: {a} + {b} = {a + b}")
                return False

def main():
    user_level = int(get_level())
    user_number_of_questions = int(get_number_of_questions())
    correct = 0
    for i in range(user_number_of_questions):
        if(run_game(user_level)):
            correct += 1
    percent_correct = correct * 100 / user_number_of_questions
    print(f"You got {correct} out of {user_number_of_questions} questions correct: {percent_correct:.2f}%")

main()
