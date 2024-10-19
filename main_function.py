

def calculate_monthly_income(loan_amount, part_time_income, job_status):
    if job_status == True:
        return (loan_amount / 12) + float(part_time_income)
    else:
        return (loan_amount / 12)
    

def calculate_enough_money(amount, bank_account):
    if amount > bank_account:
        return False
    else:
        return True

def savings(bank_account, savings_account, monthly_income):
    saving_money = input("Do you want to add money to savings 'yes' or 'no'\n")
    if saving_money == "yes":
        saving_money_options = input("Do you want to make a one off transfer or monthly transfer? Please enter 'one off' or 'monthly'\n")
        if saving_money_options == "one off":
            saving_money_amount = input("How much do you want to transfer to savings?\n")
            if not calculate_enough_money(float(saving_money_amount), bank_account):
                print("Sorry you do not have enough money in your bank account to transfer to savings\n")
                return bank_account, savings_account, monthly_income
            else:
                savings_account += float(saving_money_amount)
                bank_account -= float(saving_money_amount)
        else:
            saving_money_amount = input("How much do you want to transfer to savings per month? You currently have "+ str(bank_account) +" in your bank account and "+str(savings_account)+" in savings\n")
            if not calculate_enough_money(float(saving_money_amount), monthly_income):
                print("Sorry you do not have enough money in your monthly income to transfer to savings\n")
                return bank_account, savings_account, monthly_income
            else:
                savings_account += float(saving_money_amount)
                monthly_income -= float(saving_money_amount)
    else:   
        print("Okay! No money has been added to savings\n")
    return bank_account, savings_account, monthly_income
            
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Variables
    bank_account = 0
    job_status = False
    loan_amount = 0
    part_time_income = 0
    savings_account = 0

    # Get maintenance/student loan from user
    print("Hi! Welcome to the best financial simulator game ever!\n")
    loan_amount = int(input("Lets get started! How much maintenance/student loan do you have per year?\n"))
    # Get their job status, are they working a part time job?
    job_status = input("Are you currently working a part-time job? Please enter 'yes' or 'no'\n")
    # Change job_status based on input
    if job_status == "yes":
        job_status = True
        part_time_income = input("What is your part-time income per month?\n")
    else:
        job_status = False

    monthly_income = calculate_monthly_income(loan_amount, part_time_income, job_status)
    print(f"Okay! Your monthly income is: £{monthly_income:.2f}")

    bank_account, savings_account, monthly_income = savings(bank_account, savings_account, monthly_income)




