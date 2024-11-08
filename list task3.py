#3. Write a Python program to find duplicate values from a list and display those.

def find_duplicates(numbers):
    # Initialize an empty list to store duplicates
    duplicates = []
    
    # Loop through each element in the list
    for i in range(len(numbers)):
        # Check if the current element appears again in the remaining list
        if numbers[i] in numbers[i + 1:] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])
    
    return duplicates

# Example usage
my_list = [1, 2, 3, 4, 2, 5, 3, 6, 1]
duplicates = find_duplicates(my_list)
print("Duplicate values:", duplicates)
