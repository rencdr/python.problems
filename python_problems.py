""" 1.Two Sum- Given an array of numbers, find the two numbers such that they add up to a specific target. 
def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
"""
"""
2.Reverse Integer- Reverse an integer. For example, reverse 123 to get 321.

def reverse_integer(x):
    sign = 1 if x >= 0 else -1
    x = abs(x)
    reversed_x = int(str(x)[::-1])
    reversed_x *= sign
    return reversed_x if -(2**31) <= reversed_x <= (2**31) - 1 else 0


"""