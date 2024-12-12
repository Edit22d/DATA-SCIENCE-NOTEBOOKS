
# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a 
# temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 
def tempereture_classifier():
    temperature = float(input('Enter the temperature values in °C:\t'))
    if temperature < 0:
        print('freezing')
    elif 0 >= temperature <= 10:
        print('cold')
    elif 11 >= temperature <= 20:
        print('moderate')
    elif 21 >= temperature <= 30:
        print('warm')
    else:
        print("hot")
tempereture_classifier()
        
# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2.
# What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the 
# answer in 1 decimal place
def volume_of_a_sphere ():
    radius = int(input('Enter the radius of a sphere:\t'))
    import math
    pie = math.pi
    volume = (4/3)*pie*radius**2
    print(f'The volume of a sphere with{pie} and {radius**2} is {volume:.2f}')
volume_of_a_sphere()