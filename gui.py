"""
Kristian K. Damsgaard, 2019.

Simple GUI for the mortgage calculator.
"""

import tkinter as tk
import sys

from calculator import MortgageCalculator as Calculator
from log import Log

class MortgageGUI:
    def __init__(self):

        self._principal = None
        self._payment = None
        self._interest = None
        self._payments = None
        self._cost = None
        self._total = None

        self._log = Log()
        self._calculator = Calculator()

        #Master
        self._master = tk.Tk()
        self._master.title("Mortgage Calculator")

        #Principal
        tk.Label(self._master, text="Principal:").grid(row=0)
        self._entry_principal = tk.Entry(self._master)
        self._entry_principal.grid(row=0, column=1, padx=5, pady=5)
        self._button_principal = tk.Button(self._master, text="Calculate", command=self.calculate_present_value)
        self._button_principal.grid(row=0, column=2, padx=5)
        
        #Monthly payment
        tk.Label(self._master, text="Monthly payment:").grid(row=1)
        self._entry_payment = tk.Entry(self._master)
        self._entry_payment.grid(row=1, column=1, padx=5, pady=5)
        self._button_payment = tk.Button(self._master, text="Calculate", command=self.calculate_payment)
        self._button_payment.grid(row=1, column=2, padx=5)

        #Interest
        tk.Label(self._master, text="Interest (%/year):").grid(row=2)
        self._entry_interest = tk.Entry(self._master)
        self._entry_interest.grid(row=2, column=1, padx=5, pady=5)
        self._button_interest = tk.Button(self._master, text="Calculate", command=self.calculate_interest)
        self._button_interest.grid(row=2, column=2, padx=5)

        #Amount of payments
        tk.Label(self._master, text="Total monthly payments:").grid(row=3)
        self._entry_payments = tk.Entry(self._master)
        self._entry_payments.grid(row=3, column=1, padx=5, pady=5)
        self._button_payments = tk.Button(self._master, text="Calculate", command=self.calculate_payments)
        self._button_payments.grid(row=3, column=2, padx=5)

        tk.Label(self._master, text="Total years in debt:").grid(row=4)
        self._entry_payments_years = tk.Entry(self._master)
        self._entry_payments_years.grid(row=4, column=1, padx=5, pady=5)


        #Cost of loan
        tk.Label(self._master, text="Cost of loan:").grid(row=5)
        self._entry_cost = tk.Entry(self._master)
        self._entry_cost.grid(row=5, column=1, padx=5, pady=5)
        # self._button_cost = tk.Button(self._master, text="Calculate", command=self.calculate_cost)
        # self._button_cost.grid(row=4, column=2, padx=5, pady=5)

        #Grand total
        tk.Label(self._master, text="Grand total:").grid(row=6)
        self._entry_total = tk.Entry(self._master)
        self._entry_total.grid(row=6, column=1, padx=5, pady=5)
        # self._button_total = tk.Button(self._master, text="Calculate", command=self.calculate_cost)
        # self._button_total.grid(row=5, column=2, padx=5, pady=5)

        #Messages
        self._message = tk.Label(self._master, text="")
        self._message.grid(row=7, columnspan=3)

        #Exit
        self._button_exit = tk.Button(self._master, text="Exit", bg="red", width=20, command=self.exit_application)
        self._button_exit.grid(row=8, columnspan=3, pady=10)

        #Main loop
        self._master.mainloop()

    def calculate_present_value(self):
        self._payment = self._entry_payment.get()
        self._interest = self._entry_interest.get()
        self._payments = self._entry_payments.get()

        try:
            self._payment = float(self._payment)
            self._interest = float(self._interest)
            self._payments = float(self._payments)
            self._principal = self._calculator.calculate_present_value(self._payment, self._interest, self._payments)
            self._entry_principal.delete(0, tk.END)
            entry = str(round(self._principal, 2))
            self._entry_principal.insert(0, entry)
            self.calculate_grand_total()
            self.calculate_cost()    
        except ValueError:
            self._message.config(text="Enter valid numbers.")
            self._log.append_message(self, "calculate_present_value() ValueError")
                 
    def calculate_payment(self):
        self._principal = self._entry_principal.get()
        self._interest = self._entry_interest.get()
        self._payments = self._entry_payments.get()

        try:
            self._principal = float(self._principal)
            self._interest = float(self._interest)
            self._payments = float(self._payments)
            self._payment = self._calculator.calculate_monthly_payment(self._principal, self._interest, self._payments)
            self._entry_payment.delete(0, tk.END)
            entry = str(round(self._payment, 2))
            self._entry_payment.insert(0, entry)
            self.calculate_grand_total()
            self.calculate_cost()
        except ValueError:
            self._message.config(text="Enter valid numbers.")
            self._log.append_message(self, "calculate_payment() ValueError")

    def calculate_interest(self):
        self._principal = self._entry_principal.get()
        self._payment = self._entry_payment.get()
        self._payments = self._entry_payments.get()
        
        try:
            self._principal = float(self._principal)
            self._payment = float(self._payment)
            self._payments = float(self._payments)
            self._interest = self._calculator.calculate_interest(self._principal, self._payment, self._payments)
            
            self._entry_interest.delete(0, tk.END)
            
            if self._interest == -1:
                entry = "Error"
                self._message.config(text="Enter valid numbers.")
            else:
                entry = "Approx. " + str(round(self._interest, 2))
                self.calculate_grand_total()
                self.calculate_cost()

            self._entry_interest.insert(0, entry)

        except ValueError:
            self._message.config(text="Enter valid numbers.")
            self._log.append_message(self, "calculate_payment() ValueError")

    def calculate_payments(self):
        self._principal = self._entry_principal.get()
        self._payment = self._entry_payment.get()
        self._interest = self._entry_interest.get()
        
        try:
            self._principal = float(self._principal)
            self._payment = float(self._payment)
            self._interest = float(self._interest)
            self._payments = self._calculator.calculate_number_of_payments(self._principal, self._interest, self._payment)
            self._entry_payments.delete(0, tk.END)
            entry = str(round(self._payments, 1))
            self._entry_payments.insert(0, entry)
            self._entry_payments_years.insert(0, round(self._payments/12, 2))
            self.calculate_grand_total()
            self.calculate_cost()
        except ValueError:
            self._message.config(text="Enter valid numbers.")
            self._log.append_message(self, "calculate_payments() ValueError")

    def calculate_cost(self):
        try:
            self._cost = self._total - self._principal
            self._entry_cost.delete(0, tk.END)
            entry = str(round(self._cost, 2))
            self._entry_cost.insert(0, entry)
            # self._message.config(text="Cost of loan: " + entry)
        except:
            self._message.config(text="Unknown error")
            self._log.append_message(self, "calculate_cost() uknown error")

    def calculate_grand_total(self):
        try:
            self._total = self._payments * self._payment
            self._entry_total.delete(0, tk.END)
            entry = str(round(self._total, 2))
            self._entry_total.insert(0, entry)
            # self._message.config(text="Number of payments: " + entry)
        except:
            self._message.config(text="Unknown error")
            self._log.append_message(self, "calculate_grand_total() uknown error")
    def exit_application(self):
        sys.exit()