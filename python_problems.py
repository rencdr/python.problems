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
"""
3.Palindrome Number-Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

def is_palindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]


"""

"""
4.Roman to Integer- Convert a Roman numeral to an integer. Input is guaranteed to be within the range from 1 to 3999.

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for char in s:
        value = roman_dict[char]
        result += value
        if value > prev_value:
            result -= 2 * prev_value
        prev_value = value
    return result


"""
"""
5.Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

def are_you_playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

"""

"""
6.Clock shows h hours, m minutes and s seconds after midnight.
Your task is to write a function which returns the time since midnight in milliseconds.

def past(h, m, s):
    total_s = (h * 3600) + (m * 60) + s
    ms = total_s * 1000
    return ms
    
"""

