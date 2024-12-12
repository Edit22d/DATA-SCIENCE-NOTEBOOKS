
#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.
def favorite_foods():
    favorite_foods = ['liver','fish','beans','meat','potato','rice']
    favorite_foods.append('matooke')
    favorite_foods.append('banana')
    favorite_foods.remove('meat')
    print(f' updated favorite foods lists:',favorite_foods )
favorite_foods()

#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.
def list_numbers():
    numbers = [2, 5, 8, 10, 3, 6]
    print(f'first elements',numbers[0])
    print(f'last element',numbers[-1])
    print(f'reversed list',numbers[::-1])
    print(f'sum of all elements:',sum(numbers))
list_numbers()
    