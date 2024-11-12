def two_sum(nums, target):
    # Dictionary to store numbers and their indices
    num_to_index = {}
    
    for i, num in enumerate(nums):
        # Calculate the required number to reach the target
        diff = target - num
        # Check if the required number is already in the dictionary
        if diff in num_to_index:
            # Return indices of the two numbers
            return [num_to_index[diff], i]
        # Store the current number with its index in the dictionary
        num_to_index[num] = i

# Example usage
nums = [2, 7, 11, 15]
target = 9
print("Indices:", two_sum(nums, target))  # Output: [0, 1]