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

"""
7.Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    words = name.split()
    initials = words[0][0].upper() + '.' + words[1][0].upper()
    return initials
"""
"""
8.You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    n -= 1  
                    i += 2  
                else:
                    i += 1  
            else:
                i += 2
        
        return n <= 0
"""

"""
9.There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)  
        
        result = [candy + extraCandies >= max_candies for candy in candies]

        return result

"""
"""
10.Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and s[left].lower() not in vowels:
                left += 1
            while left < right and s[right].lower() not in vowels:
                right -= 1
            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)

"""
"""
11.Determine if the poker hand is flush, meaning if the five cards are of the same suit.
Your function will be passed a list/array of 5 strings, each representing a poker card in the format "5H" (5 of hearts), meaning the value of the card followed by the initial of its suit (Hearts, Spades, Diamonds or Clubs). No jokers included.
Your function should return true if the hand is a flush, false otherwise.
The possible card values are 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

def is_flush(cards):
    if not cards:
        return False
    
    suit = cards[0][-1]
    
    for card in cards:
        if card[-1] != suit:
            return False
    
    return True
"""
"""
12.Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:n, n is the number of hotdogs a customer will buy, different numbers have different prices (refer to the following table), return how much money will the customer spend to buy that number of hotdogs.
def sale_hotdogs(n):
    if n < 5:
        return n * 100  
    elif 5 <= n < 10:
        return n * 95   
    elif n >= 10:
        return n * 90   
"""
