# Question 2(i)


# Define a function named calculate_bmi that takes a person's weight 
# (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
def calculate_bmi():
    weight = int(input('Enter weight in kilograms:\t'))
    height = int(input('Enter height in metres:\t'))
    BMI = weight / height
    if BMI < 18.5:
        print('Underweight')
    elif 18.5 >= BMI >= 24.9:
        print('Normal weight')
    elif 25 >= BMI >= 29.9:
        print('Overweight')
    else:
        print('Obese')
calculate_bmi()

# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a 
# function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use 
# the real pie value (import math)
def volume_of_a_cylinder():
    r = int(input('Enter the radius of a cylinder:\t'))
    h=int(input('Enter the height of a cylinder:\t'))
    import math
    pie = math.pi
    v = pie*(r**2)*h
    print(f'The volume of a cylinder with {r**2} and {h} is {v:.1f}')
volume_of_a_cylinder()
    
    
