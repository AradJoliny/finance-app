

def calculate_monthly_income(loan_amount, part_time_income, job_status):
    if job_status == True:
        return (loan_amount / 12) + float(part_time_income)
    else:
        return (loan_amount / 12)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Variables
    job_status = False
    loan_amount = 0
    part_time_income = 0
    bank_account = 0
    savings_account = 0
    current_month = 0
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

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

    while current_month <= 11:
        bank_account += monthly_income
        while (bank_account + savings_account) > 0:
            print("Month:", months[current_month])

    print(f"Okay! Your monthly income is: £{monthly_income:.2f}")




