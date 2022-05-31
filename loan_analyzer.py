# coding: utf-8
import csv
from pathlib import Path
from webbrowser import get

"""Part 1: Automate the Calculations."""

# loan portfolio
loan_costs = [500, 600, 200, 1000, 450]

# Totals and prints the number of loans in the portfolio
total_number_of_loans = len(loan_costs)
print("The total number of outstanding loans is: ", total_number_of_loans)

# Prints the total value of the loans
total_loan_amounts = sum(loan_costs)
print(f"The total amount of all outstanding loans is: ${total_loan_amounts}")

# Prints the average loan amount
average_loan_amount = total_loan_amounts / total_number_of_loans
print(f"The average loan amount is: ${average_loan_amount: .2f}")


"""Part 2: Analyze Loan Data."""

# loan data for present value calculation
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Print each variable.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print("The future value is: $", future_value)
print(f"There are {remaining_months} months remaining")


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
discount_rate = .20
fair_value = future_value / (1 + (discount_rate/12))**remaining_months

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_price = loan.get("loan_price")
if fair_value >= loan_price:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")


"""Part 3: Perform Financial Calculations."""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#    The function should return the `present_value` for the loan.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate/12))**remaining_months
    return present_value

#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
annual_discount_rate = .20
pv = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)
print(f"The present value of the loan is: ${pv: .2f}")

"""Part 4: Conditionally filter lists of loans."""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Creates an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loops through all the loans and appends any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

# Prints the `inexpensive_loans` list
print(inexpensive_loans)

"""Part 5: Save the results."""

# Sets the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Sets the output file path
output_path = Path("inexpensive_loans.csv")

# Creates new csv file with values from the inexpensive loan list.
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)

    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

