# Tip Calculator
print("Welcome to the tip calculator")  # Welcome Message
bill = float(input("What was the total bill?\n"))  # Get bill amount
# Get tip percentage
tip_percentage = int(
    input("How much tip would you like to give? 10, 12 or 15\n"))
tip_amount = bill * (tip_percentage / 100)  # Calculate tip amount
total_bill = bill + tip_amount  # Calculate total bill with tip
# Get number of people
people = int(input("How many people to split the bill with?\n"))
final = total_bill / people  # Split among people
print(f"Each person should pay:  ${final}")  # Display final amount per person
