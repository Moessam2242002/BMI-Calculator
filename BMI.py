def get_user_input():
    while True:
        print("""Choose 
                1 ==> kg, meter
                2 ==> pound, feet
            """)
        choice = input("Choose number: ")
        
        try:
            if choice == '1':
                weight = float(input("Enter weight in kilograms: "))
                height = float(input("Enter height in meters: "))
            elif choice == '2':
                weight = float(input("Enter weight in pounds: "))
                height = float(input("Enter height in feet: "))
                weight *= 0.453592  # Convert pounds to kilograms
                height *= 0.3048    # Convert feet to meters
            else:
                print("Invalid choice. Please try again.")
                continue
            
            if weight <= 0 or height <= 0:
                print("Please enter positive values.")
            else:
                return weight, height
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_weight_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def suggest_weight_range(bmi, height):
    if bmi < 18.5:
        return f"Your weight should increase to at least {18.5 * (height ** 2):.2f} kg for a normal BMI."
    elif bmi >= 25:
        return f"Your weight should decrease to at most {24.9 * (height ** 2):.2f} kg for a normal BMI."
    else:
        return "You are in Normal weight."

def visualize_bmi(bmi):
    print("\nScale:")
    print("""
    | Underweight | Normal weight | Overweight | Obese |
    |   < 18.5    |  18.5 - 24.9  |  25 - 29.9 |  > 30 |
    """)
    position = max(min(int((bmi - 10) * 2), 46), 10)  
    print(f"{' ' * position}⬆ Your BMI = {bmi:.2f}")
weight, height = get_user_input()
bmi = calculate_bmi(weight, height)
weight_category = get_weight_category(bmi)

print(f"Calculated BMI = {bmi:.2f} and weight category is {weight_category}.")
print(suggest_weight_range(bmi, height))
visualize_bmi(bmi)
