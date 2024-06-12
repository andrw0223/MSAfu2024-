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
