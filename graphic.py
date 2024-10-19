import tkinter as tk
from tkinter import messagebox

def graphic_interface():
    # Initialize the main window
    root = tk.Tk()
    root.title("Financial Simulator")

    # Create frames for organizing widgets
    frame = tk.Frame(root)
    frame.pack()
    root.mainloop()
    
    


if __name__ == '__main__':
    global bank_account, job_status, loan_amount, part_time_income, savings_account, current_month, months, happiness_level
    bank_account = 0
    job_status = False
    loan_amount = 0
    part_time_income = 0
    savings_account = 0
    current_month = 0
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    happiness_level = 0
    graphic_interface()
