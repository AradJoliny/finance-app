
import sys

from scenarios_list import scenarios  # Import the scenarios list
import time
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.terminal = sys.stdout  # Save the original stdout

    def write(self, message):
        self.text_widget.insert(tk.END, message)  # Write to Tkinter Text widget
        self.text_widget.see(tk.END)  # Auto-scroll to the end
        self.terminal.write(message)  # Write to terminal as well

    def flush(self):
        pass  # Needed for file-like behavior

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
        saving_money_options = input \
            ("Do you want to make a one off transfer or monthly transfer? Please enter 'one off' or 'monthly'\n")
        if saving_money_options == "one off":
            saving_money_amount = input("How much do you want to transfer to savings?\n")
            if not calculate_enough_money(float(saving_money_amount), bank_account):
                print("Sorry you do not have enough money in your bank account to transfer to savings\n")
                return bank_account, savings_account, monthly_income
            else:
                savings_account += float(saving_money_amount)
                bank_account -= float(saving_money_amount)
        else:
            saving_money_amount = input \
                ("How much do you want to transfer to savings per month? You currently have  "+ str
                    (bank_account) +" in your bank account and " + str(savings_account) + " in savings\n")
            if not calculate_enough_money(float(saving_money_amount), monthly_income):
                print("Sorry you do not have enough money in your monthly income to transfer to savings\n")
                return bank_account, savings_account, monthly_income
            else:
                savings_account += float(saving_money_amount)
                monthly_income -= float(saving_money_amount)
    else:
        print("Okay! No money has been added to savings\n")
    return bank_account, savings_account, monthly_income


def create_popup(image_path):
    # Create the root window
    root = tk.Tk()
    root.title("Popup with Image and Terminal Output")

    # Load the image
    img = Image.open(image_path)
    img = img.resize((250, 250))  # Resize the image if necessary
    img = ImageTk.PhotoImage(img)

    # Create a label to display the image
    image_label = Label(root, image=img)
    image_label.pack()

    # Create a Text widget to display terminal output
    text_widget = tk.Text(root, wrap='word', height=10, padx=10, pady=10)
    text_widget.pack()

    # Redirect sys.stdout to our custom class
    sys.stdout = RedirectText(text_widget)

    # Start the Tkinter event loop
    root.mainloop()


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

    image_path = "/Users/aradjoliny/Downloads/photo-1529778873920-4da4926a72c2.jpeg"  # Replace with your image path
    create_popup(image_path)  # This will start the GUI window

    # Get maintenance/student loan from user
    print("Hi! Welcome to the best financial simulator game ever!\n")
    loan_amount = int(input("Lets get started! How much maintenance/student loan do you have per year?\n"))
    # Get their job status, are they working a part-time job?
    job_status = input("Are you currently working a part-time job? Please enter 'yes' or 'no'\n")
    # Change job_status based on input
    if job_status == "yes":
        job_status = True
        part_time_income = input("What is your part-time income per month?\n")
    else:
        job_status = False

    monthly_income = calculate_monthly_income(loan_amount, part_time_income, job_status)
    print(f"Okay! Your monthly income is: £{monthly_income:.2f}")

    # Get rent and food budget from user
    food_budget = float(input("How much do you want to set aside for food per month? For reference, the average UK "
                              "uni student spends £144.00 per month on groceries.\n"))
    if food_budget > monthly_income:
        print("You can't spend more than you earn, on food! Try again.")
    rent_budget = float(input("How much is your monthly rent amount?\n"))
    if rent_budget + food_budget > monthly_income:
        print("I don't think you can afford to live here... Try again.")

    # Print monthly budget after expenses
    print("\nTherefore your monthly budget after expenses is: £", (monthly_income - food_budget - rent_budget))

    bank_account += monthly_income - food_budget - rent_budget

    # Initialise bank account after deductions
    while current_month < 12:
        while bank_account > 0:
            while happiness_level > 0:
                time.sleep(1.5)
                print("Month: ", months[current_month])
                time.sleep(1)
                print("\nBank account balance: £", bank_account)
                time.sleep(1)
                print("\nSavings account balance: £", savings_account)
                time.sleep(1)
                print("\nYour happiness level: ", happiness_level, "\n")
                time.sleep(1)

                bank_account, savings_account, monthly_income = savings(bank_account, savings_account, monthly_income)
                happiness_level -= 10

            current_month += 1
            bank_account += monthly_income - food_budget - rent_budget



