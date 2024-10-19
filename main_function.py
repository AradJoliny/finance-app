import random
import sys

from scenarios_list import scenarios  # Import the scenarios list.
import time
from scenarios_list import scenarios

def validate_yes_no(message):
    valid = False
    while valid == False:
        choice = input(message)
        if choice.lower() == "yes":
            valid = True
        elif choice.lower() == "no":
            valid = True
        else:
            print("Please enter yes or no")
    return choice

def validate_budgets(prompt,message,income):
    valid = False
    while valid == False:
        budget = float(input(prompt))
        if budget > income:
            print(message)
        else:
            valid = True
    return budget

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
    saving_money = validate_yes_no("Do you want to add money to savings 'yes' or 'no'\n")
    if saving_money == "yes":
        saving_money_amount = input("How much do you want to transfer to savings?\n")
        if not calculate_enough_money(float(saving_money_amount), bank_account):
            print("Sorry you do not have enough money in your bank account to transfer to savings\n")
            return bank_account, savings_account, monthly_income
        else:
            savings_account += float(saving_money_amount)
            bank_account -= float(saving_money_amount)
    else:
        print("Okay! No money has been added to savings\n")
    return bank_account, savings_account, monthly_income


def random_events():
    # 25% chance to go out tonight
    if random.random() <= 0.25:
        print("You have the option to out clubbing tonight! Do you want to go? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            print("You went out and had a great time!\n Money lost: -50, Happiness gained: +20")
            return -50, +20  # Deduct some money and increase happiness
        else:
            print("You decided not to go to the party. You got some bad FOMO...")
            return -0, -25  # Deduct no money but decrease happiness

    # 15% chance it's your friend's birthday
    if random.random() <= 0.15:
        print("It's your friend's birthday! Do you want to buy them a gift? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            print("You bought a gift for your friend! It cost you some money but they really appreciated it.\n Money lost: -25, Happiness gained: +10")
            return -25, +10  # Deduct money and increase happiness
        else:
            print("You decided not to buy a gift for your friend.")

    # 10% chance a new Mario Kart game just came out
    if random.random() <= 0.20:
        print("A new Mario Kart game just came out! Do you want to buy it? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            print("You bought the new Mario Kart game! It was expensive but it's a lot of fun.\n Money lost: -50, Happiness gained: +15")
            return -50, +15  # Deduct money and increase happiness
        else:
            print("You decided not to buy the new Mario Kart game.")

    return 0, 0  # No change if none of the events happen

    # 50% chance to go for a takeout
    if random.random() <= 0.20:
        print("You have the option to go for a takeout! Do you want to go? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            print("You went for a takeout and had some great scran! But it cost you some money.\nMoney lost: -15, Happiness gained: +20")
            return -15, +20  # Deduct some money and increase happiness
        else:
            print("You decided not to go for a takeout.")

def after_uni(savings_account):
    savings_account = savings_account * (1.02**4)
    print("After 4 years of uni, your savings account balance is: £", savings_account)
    savings_choice = input("Do you want to make a Life Time ISA or invest in an index fund? Please enter 'ISA' or 'index fund'\n")
    if savings_choice == "ISA":
        savings_account = savings_account * (1.01**30)
        print("After 30 years, your savings account balance is: £", savings_account)
        print("You could have earned more money if you invested in an index fund (7% return) instead of a Life Time ISA (1% return), but you didn't take the risk!")
    else:
        savings_account = savings_account * (1.07**30)
        print("After 30 years, your savings account balance is: £", savings_account)
        print("You earned more money because you invested in an index fund (7% return) instead of a Life Time ISA (1% return), well done, but this could have gone the other way!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Variables
    bank_account = 0
    job_status = False
    loan_amount = 0
    part_time_income = 0
    savings_account = 0
    current_month = 0
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    happiness_level = 100

    # Get maintenance/student loan from user
    print("Hi! Welcome to the best financial simulator game ever!\n")
    loan_amount = int(input("Lets get started! How much maintenance/student loan do you have per year?\n"))
    # Get their job status, are they working a part-time job?
    job_status = validate_yes_no("Are you currently working a part-time job? Please enter 'yes' or 'no'\n")
    # Change job_status based on input
    if job_status == "yes":
        job_status = True
        part_time_income = input("What is your part-time income per month?\n")
    else:
        job_status = False

    monthly_income = calculate_monthly_income(loan_amount, part_time_income, job_status)
    print(f"Okay! Your monthly income is: £{monthly_income:.2f}")

    # Get rent and food budget from user
    food_budget = validate_budgets("How much do you want to set aside for food per month? For reference, the average UK ""uni student spends £144.00 per month on groceries.\n","You can't spend more than you earn, on food! Try again.",monthly_income)
    rent_budget = validate_budgets("How much is your monthly rent amount?\n","I don't think you can afford to live here... Try again.",monthly_income)

    # Print monthly budget after expenses
    print("\nTherefore your monthly budget after expenses is: £", (monthly_income - food_budget - rent_budget))

    bank_account += monthly_income - food_budget - rent_budget

    # Initialise bank account after deductions

    for month in months:
        if happiness_level > 0 and bank_account > 0:
            time.sleep(1.5)
            print(month)
            time.sleep(1)
            print("\nBank account balance: £", bank_account)
            time.sleep(1)
            print("\nSavings account balance: £", savings_account)
            time.sleep(1)
            print("\nYour happiness level: ", happiness_level, "\n")
            time.sleep(1)

            # crazy unavoidable event
            scenario_i = random.randint(0, 11)
            print(scenarios[scenario_i][0])
            bank_account += scenarios[scenario_i][1]

            # Call the random events function
            money_change, happiness_change = random_events()
            bank_account += money_change
            happiness_level += happiness_change

            if bank_account < 0:
                print("Uh oh! You have no money left in your bank account. You have lost the game.")
                sys.exit()

            bank_account, savings_account, monthly_income = savings(bank_account, savings_account, monthly_income)
            happiness_level -= 10

            bank_account += monthly_income - food_budget - rent_budget
        elif happiness_level <= 0:
            print("You are too unhappy to continue. You have lost the game.")
            break
        else:
            print("You have run out of money. You have lost the game.")
            break

    after_uni(savings_account)
