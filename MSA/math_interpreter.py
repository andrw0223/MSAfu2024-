def main():
    expression = input("Expression: ").split(" ")
    if (not len(expression) == 3):
        print("ERROR: Please enter in 3 characters seperated by a space")

        a = float(expression[0])

    sign = expression[1]
    if (sign == '+'):
        answer = float(expression[0] + expression[2])
        print(f"{answer}")
    
    if (sign == '-'):
        answer = float(expression[0] - expression[2])
        print(f"{answer}")
    
    
    if (sign == '*'):
        answer = float(expression[0] * expression[2])
        print(f"{answer}")
    
    
    if (sign == '/'):
        answer = float(expression[0] / expression[2])
        print(f"{answer}")
    else:
        print("ERROR: Please enter a operator in the second character")
    
    




main()
