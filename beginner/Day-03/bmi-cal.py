# BMI Calculator

weight = int(input("Hey! Can you tell me your weight in kg?"))  # Get weight
# Get height
height = float(
    input("And how tall are you? Centimeter would be perfect!")) / 100
bmi = weight / height ** 2  # Calculate BMI

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f} and you are classified as Under weight.")
elif bmi < 24.9:
    print(f"Your BMI is {bmi:.2f} and you are classified as Normal weight.")
elif bmi < 29.9:
    print(f"Your BMI is {bmi:.2f} and you are classified as Over weight.")
else:
    print(f"Your BMI is {bmi:.2f} and you are classified as Obesity.")
