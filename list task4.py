'''4. Write a Python program to split a given list into two parts where the length of the first
part of the list is given.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splitted the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])'''
def split_list(numbers, length_first_part):
    # Split the list into two parts based on the specified length
    first_part = numbers[:length_first_part]
    second_part = numbers[length_first_part:]
    
    return first_part, second_part

# Example usage
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3

first_part, second_part = split_list(original_list, length_of_first_part)
print("Original list:", original_list)
print("Length of the first part of the list:", length_of_first_part)
print("Splitted the list into two parts:", (first_part, second_part))

