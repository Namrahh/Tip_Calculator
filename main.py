# Billing Tip Calculator

print("welcome to the tip calculator")
bill = float(input("enter your bill amount: "))
people = int(input("enter the number of people: "))
tip = int(input("how much tip would you like to pay? 10, 20, 25"))
tip_as_percent = int(tip/100)
total_tip_amount = int(bill) * int(tip_as_percent)
total_bill=int(bill)+int(total_tip_amount)
bill_per_person = int(total_bill)/int(people)
final_amount = round(bill_per_person, 2)
print(f"each person should pay: {bill_per_person}")