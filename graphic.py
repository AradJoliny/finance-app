import tkinter as tk
from tkinter import messagebox

def graphic_interface():
    # Initialize the main window
    root = tk.Tk()
    root.title("Financial Simulator")

    # Create frames for organizing widgets
    frame = tk.Frame(root)
    frame.pack()

    # Variables for user inputs
    loan_amount_var = tk.DoubleVar()
    part_time_income_var = tk.DoubleVar()
    job_status_var = tk.StringVar()
    savings_account_var = tk.DoubleVar()
    bank_account_var = tk.DoubleVar(value=0)

    # Welcome message
    label1 = tk.Label(frame, text="Hi! Welcome to the best financial simulator game ever!")
    label1.pack()

    # Input for loan amount
    label2 = tk.Label(frame, text="How much maintenance/student loan do you have per year?")
    label2.pack()
    loan_amount_entry = tk.Entry(frame, textvariable=loan_amount_var)
    loan_amount_entry.pack()

    # Input for job status as radio buttons
    label3 = tk.Label(frame, text="Are you currently working a part-time job?")
    label3.pack()
    job_status_yes = tk.Radiobutton(frame, text="Yes", variable=job_status_var, value="yes")
    job_status_no = tk.Radiobutton(frame, text="No", variable=job_status_var, value="no")
    job_status_yes.pack()
    job_status_no.pack()
    #get job status
    if job_status_var.get() == "yes":
        job_status = True
    else:
        job_status = False

    # Input for part-time income
    label4 = tk.Label(frame, text="What is your part-time income per month?")
    label4.pack()
    part_time_income_entry = tk.Entry(frame, textvariable=part_time_income_var)
    part_time_income_entry.pack()

    # Submit button
    submit_button = tk.Button(frame, text="Submit", command=lambda: calculate_monthly_income(
        loan_amount_var.get(), part_time_income_var.get(), job_status_var.get()))
    submit_button.pack()

    # Frame for savings information
    frame2 = tk.Frame(root)
    frame2.pack()

    # savings as radio buttons
    label5 = tk.Label(frame2, text="Do you want to add money to savings?")
    label5.pack()
    saving_money_yes = tk.Radiobutton(frame2, text="Yes", variable=savings_account_var, value="yes")
    saving_money_no = tk.Radiobutton(frame2, text="No", variable=savings_account_var, value="no")
    saving_money_yes.pack()
    saving_money_no.pack()
    if savings_account_var.get() == "yes":
        saving_money = True
    else:
        saving_money = False
    if saving_money:
        saving_money_entry = tk.Entry(frame2)
    # Button to process savings
        save_button = tk.Button(frame2, text="Submit Savings", command=lambda: process_savings(saving_money_entry.get(), bank_account_var.get(), savings_account_var.get()))
        save_button.pack()

    # Start the GUI loop
    root.mainloop()

def calculate_monthly_income(loan_amount, part_time_income, job_status):
    # Determine if the user is employed
    is_employed = job_status.lower() == 'yes'
    
    # Calculate monthly income
    if is_employed:
        monthly_income = (loan_amount / 12) + part_time_income
    else:
        monthly_income = (loan_amount / 12)

    # Show monthly income in a message box
    messagebox.showinfo("Monthly Income", f"Okay! Your monthly income is: £{monthly_income:.2f}")
    return monthly_income

def process_savings(save_choice, bank_account, savings_account):
    # Process savings based on user input
    if save_choice.lower() == "yes":
        saving_amount = float(input("How much do you want to transfer to savings?\n"))
        
        # Check if there are enough funds in the bank account
        if saving_amount > bank_account:
            messagebox.showerror("Insufficient Funds", "Sorry, you do not have enough money in your bank account to transfer to savings.")
        else:
            savings_account += saving_amount
            bank_account -= saving_amount
            messagebox.showinfo("Savings Update", f"Transferred £{saving_amount} to savings.\nCurrent Savings: £{savings_account}\nCurrent Bank Account: £{bank_account}")
    else:
        messagebox.showinfo("Savings Update", "Okay! No money has been added to savings.")

if __name__ == '__main__':
    graphic_interface()
