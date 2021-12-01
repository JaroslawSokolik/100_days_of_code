# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? PLN "))
tip = int(input("What percentage of the tip you would like to give? 10, 15, 20? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_bill = round(bill_per_person, 2)
final_bill_with_formatting = '{0:.2f}'.format(final_bill)
print(f"The total amount to pay by each person is {final_bill_with_formatting} PLN")


