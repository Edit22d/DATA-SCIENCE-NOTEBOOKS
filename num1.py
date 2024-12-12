# #calculate area of a circle
# def caculate_area():
#     radius = int(input('Enter the radius of the circle in parameter:\t'))
#     import math
#     pie = math.pi
#     area =math.pi*radius**2
#     print(f'The area of the circle with radius {radius**2} is {area}')
# caculate_area()
# # volume of sphere 
# def volume_sphere():
#     radius = int(input('Enter the volume of the sphere in cm:\t'))
#     import math
#     pie = math.pi
#     volume = (4/3)*pie**radius**2
#     print(f'The volume of sphere with radius{radius**2} is {volume}')
# volume_sphere()
# calculate the sum 
def recursive_sum():
    # n = int(input('Enter a positive integer:'))
    # if n <= 0:
    #     sum = 0:
        
    #     print('Please enter a positive integer.')
    # else:
    #     print('invailed input')
    num = int(input("Enter six numbers : "))
    sum = 0
    for adition in num:
        sum+=adition
    print(f"The sum of {num} is {sum}")
recursive_sum()
    
   