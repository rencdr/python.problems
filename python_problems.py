""" 1.Two Sum Given an array of numbers, find the two numbers such that they add up to a specific target. 
def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
"""
"""


"""