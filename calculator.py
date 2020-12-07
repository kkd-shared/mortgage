"""
Kristian K. Damsgaard, 2019

Program for calculating mortgages.
"""

import math

class MortgageCalculator:
    def __init__(self):
        pass

    def calculate_present_value(self, payment, interest, payments):
        """
        Calculates the present value of the mortgage.

        PV = p * (1-(1+i)^-n) / i, where PV = present value, p = monthly payment, i is yearly interest / 100, n = amount of payments.
        """
        p = payment
        i = self.yearly_to_monthly_interest(interest) / 100
        n = payments
        return p * (1 - math.pow(1+i, -n)) / i

    def calculate_monthly_payment(self, principal, interest, payments):
        """
        Calculates the monthly payment based on principal, interest and amount of payments.

        p = P * (i / (1-(1+i)^-n)), where P = principal, p = monthly payment, i is yearly interest / 100, n = amount of payments.
        """
        big_p = principal
        i = self.yearly_to_monthly_interest(interest) / 100
        n = payments
        return big_p * i / (1 - math.pow((1+i), -n))

    def calculate_interest(self, principal, payment, payments):
        """
        Estimates the (yearly) interest on a loan based on principal, payment size and number of payments.
        """
        low_i = 0
        high_i = 100
        big_p = 0

        if payment * payments < principal:
            return -1

        while True:
            mid_i = (high_i - low_i) / 2 + low_i
            big_p = self.calculate_present_value(payment, mid_i, payments)   
            if big_p > (principal + 0.000001):
                low_i = mid_i
            elif big_p < (principal - 0.000001):
                high_i = mid_i
            else:
                return mid_i

    def calculate_number_of_payments(self, principal, interest, payment):
        """
        Calculates the number of monthly payments based on principal, interest and monthly payment.

        n = -(log(1-P*i/p)/log(1+i)), n is number of payments, P is principal, i is interestfactor (interest% / 100 + 1) and p i monthly payment
        """
        big_p = principal
        i = self.yearly_to_monthly_interest(interest) / 100
        p = payment

        if i is 0:
            return big_p / p
        else:
            upper = 1-big_p*i/p
            if upper <= 0:
                return math.inf
            else:
                return -(math.log(upper)/math.log(1+i))
                # return -(math.log(1-big_p*i/p)/math.log(1+i))

    def yearly_to_monthly_interest(self, interest):
        """
        Calcultes monthly interest (%) based on yearly interest (%).
        """
        return (math.pow(1 + (interest/100), 1/12) -1) * 100

    def monthly_to_yearly_interest(self, interest):
        """
        Calcultes yearly interest (%) based on monthly interest (%).
        """
        print(interest)
        result = (math.pow(1 + interest / 100, 12) - 1) * 100
        print(result)
        return result



    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, principal):
        self._principal = principal

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, payment):
        self._payment = payment

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, interest):
        self._interest = interest

    @property
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, payments):
        self._payments = payments
