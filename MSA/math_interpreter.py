def main():
    
    while(True):
        expression = input("Expression: ").split(" ")
        if (not len(expression) == 3):
            print("ERROR: Please enter in 3 characters seperated by a space")
            continue
        try:    
            a = float(expression[0])
            b = float(expression[2])

            sign = expression[1]
            
            if (sign == '+'):
                answer = (a + b)
                print(f"{answer}")
                break
        
            if (sign == '-'):
                answer = (a - b)
                print(f"{answer}")
                break
        
        
            if (sign == '*'):
                answer = (a * b)
                print(f"{answer}")
                break
        
        
            if (sign == '/'):
                if (b == 0):
                    print("Division by 0 is not allowed")
                    continue
                answer = (a / b)
                print(f"{answer:.2f}")
                break
            else:
                print("ERROR: Please enter a operator in the second character")
    
        except:
            print("ERROR: PLease eneter 2 integers and an operator all seperated by a space")

main()
