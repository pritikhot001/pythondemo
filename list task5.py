'''5. Write a Python program to traverse a given list in reverse order, and print the
elements with the original index.
Original list:
['red', 'green', 'white', 'black']
Traverse the said list in reverse order:
black
white
green
red'''
def traverse_reverse_with_index(items):
    # Loop through the list in reverse order with original indices
    for i in range(len(items) - 1, -1, -1):
        print(f"{items[i]} (original index: {i})")

# Example usage
original_list = ['red', 'green', 'white', 'black']
print("Original list:")
print(original_list)
print("\nTraverse the list in reverse order:")
traverse_reverse_with_index(original_list)
