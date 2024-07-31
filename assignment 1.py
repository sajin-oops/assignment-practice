# Input string of numbers delimited by commas
input_string = "1,2,3,4,5"
print(type(input_string))
#<class 'str'>
print(input_string)
#1,2,3,4,5

# Initialize an empty list to store the numbers
number_list = []

# Split the input string by commas to get individual numbers as strings
numbers = input_string.split(',')

# Iterate through the split numbers
for num in numbers:
    # If the number is an empty string, skip it
    if num == '':
        continue
    # Convert the string to an integer and add it to the list
    number_list.append(int(num))

print(number_list)
# [1, 2, 3, 4, 5]
print(type(number_list))
# <class 'list'>