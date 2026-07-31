Weight = float(input("you weight:"))
height = float(input("you height"))
bmi = weight / (height**2)

if bmi >= 30.0:
    print("Obese")
elif bmi >= 25.0:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal weight")
else:
    print("Underweight")