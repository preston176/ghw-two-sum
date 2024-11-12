# Two Sum - Interview Question Solution

## Inspiration
The **Two Sum** problem is a classic coding interview question that tests problem-solving skills and knowledge of data structures. It’s widely used because it allows interviewers to assess a candidate's approach to algorithmic efficiency, especially with hash maps. Solving this problem inspired me to explore optimized solutions and understand how hash maps can help achieve optimal time complexity.

## What it does
The **Two Sum** function takes an array of integers and a target integer as input. It finds two distinct numbers in the array that add up to the target and returns their indices. This functionality can be particularly useful in financial applications, where finding specific sum combinations quickly is essential.

## How I built it
I built this solution in Python using a hash map (dictionary) for quick lookups. As I iterate through the array, I calculate the difference between the target and each element to determine if the required complement exists in my hash map. If it does, I’ve found my answer; if not, I store the current number’s index in the hash map and continue.

## Code

```python
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
```
