#Requirements: Your program needs to: Ask the user to input from the keyboard for two inputs, one is the hours worked daily and the other is the hourly wage. Multiplying hours worked daily and hourly wage will give you the wages earned in a day.
#The two input numbers are not necessarily integers. For example, the user can enter values like 35.5 for hours worked or 17.85 for hourly wage.
#Calculate the yearly wage given the two inputs
#Note that the working hours is daily. Assume the user works 350 days per year and the same amount of hours every day.
#It would help to first write down the mathematical formula needed to calculate the yearly wage
#12% will be deducted from yearly earnings for taxes
#Print the a Pay Advice containing:
#hours worked
#hourly wage
#wages before taxes
#tax amount
#annual wages after taxes
#money values should be printed with a $ sign and all numbers should be rounded to 2 decimal places





def get_correct_number(text, must_be_less_than_24):
    bad_input = True
    user_input = 0
    while(bad_input == True):
        try:
            user_input = float(input(text))
            if user_input <=0:
                print("ERROR: Please enter a number larger than 0")
                continue
            if (user_input >24 and must_be_less_than_24):
                print("ERROR: Please enter a number less than 24")
            else:
                break
        except: print("ERROR: Please Enter a number")
    return user_input

hours_worked_daily = get_correct_number("Enter the number of hours worked daily: ", True)
hourly_wage = get_correct_number("Enter the hourly wage: ", False)

daily_wage = hours_worked_daily * hourly_wage
yearly_wage_before_tax = 350 * daily_wage

tax_percentage = 0.12
tax_amount = tax_percentage * yearly_wage_before_tax
yearly_wage_after_tax = yearly_wage_before_tax - tax_amount

print("Pay Advice \n -------------")
print(f"Hours Worked: {hours_worked_daily} \n Hourly Wage: ${hourly_wage} \n Wages Before Taxes: ${yearly_wage_before_tax:.2f} \n Tax Amount: ${tax_amount:.2f} \n Annual Wage After Taxes: ${yearly_wage_after_tax:.2f}")
