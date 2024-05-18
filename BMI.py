def bodymassindex(weight_kg, height_ft):
    height_m = height_ft * 0.3048
    bmi = weight_kg / height_m**2
    
    if bmi <= 20:
        print("You are underweight")
    elif bmi <=25:
        print("your are normal")
    elif 25 >= bmi <= 30:
        print("you are over weight")
    else:
        print("you are obeses")  
    
    return bmi

# Get user input:
weight_kg = float(input("Enter your weight in kg: "))
height_ft = float(input("Enter your height in feet: "))

print("Welcome to calculate BMI: ")

# Display results:
bmi = bodymassindex(weight_kg, height_ft)
print(f"Your BMI is:  {bmi:2f}") 


    

