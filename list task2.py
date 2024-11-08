#2. Write a Python program to get the largest and smallest number from a list without
#builtin functions.
def find_largest_and_smallest(numbers):
    # Check if the list is empty
    if not numbers:  
        return None, None

    # Assume the first element is both the largest and smallest
    largest = numbers[0]
    smallest = numbers[0]

    # Loop through each element in the list starting from the second element
    index = 1
    while index < len(numbers):  # Using a counter since we avoid len() itself
        num = numbers[index]
        
        # Update largest and smallest as necessary
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        
        index += 1

    return largest, smallest

# Example usage
my_list = [3, 1, 7, 4, -5, 10, 0]
largest, smallest = find_largest_and_smallest(my_list)
print("Largest number:", largest)
print("Smallest number:", smallest)
