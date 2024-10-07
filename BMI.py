#  1. Ask the user for their weight in kilograms and height in meters.
while True:
    print("""Choose 
            1==> kg,meter
            2==> pound,feet
        """)
    choice=(input("choose number "))
    # 1. Input validation to ensure the user enters positive numbers for weight and height.
    if choice =='1':
        weight=float(input("enter weight in kilograms "))
        height=float(input("enter height in meters "))
    elif choice=='2':
        weight=float(input("enter weight in Pounds "))
        height=float(input("enter height in Feet "))
        weight *= .453592
        height *= 0.3048
    else:
        print("invalid choice ")
        continue
    if(weight <0 or height <0):
        print("enter Positive values ")
    else :
        break
# 2. Calculate the BMI using the formula:
BMI = weight / (height **2)
"""
3. Determine the weight category based on the BMI:
    - Below 18.5: Underweight
    - 18.5 to 24.9: Normal weight
    - 25 to 29.9: Overweight
    - 30 and above: Obese
"""
w_category=""
if BMI <18.5:
    w_category="Underweight"
elif BMI>=18.5 and BMI<=24.9:
    w_category="Normal weight"
elif BMI>=25 and BMI<=29.9:
    w_category="Overweight"
elif BMI>=30:
    w_category="Obese"
# 4. Display the calculated BMI and weight category.
print(f"calculated BMI = {BMI} and weight category is {w_category} ")
# 5. Optionally, suggest a target weight range for a "Normal weight" BMI.
if BMI < 18.5:
    print(f"Your weight should increase to at least {18.5 * (height ** 2):.2f} kg for a normal BMI.")
elif BMI>=25:
    print(f"Your weight should decrease to at most {24.9 * (height ** 2):.2f} kg for a normal BMI.")
else:
    print(" You are in Normal weight")
# A visualization of the BMI scale and where the calculated BMI falls on it.
print("\nScale:")
print("""
| Underweight | Normal weight | Overweight | Obese |
|   < 18.5    |  18.5 - 24.9  |  25 - 29.9 |  > 30 |
""")
position = (BMI - 10) * 2
if position < 0:
    position = 10
elif position > 40:
    position = 46
print(f"{' ' * int(position)}⬆ Your BMI = {BMI:.2f}")
