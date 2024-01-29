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
"""
13.Write a Python function named is_anagram that takes two strings as input and returns True if the strings are anagrams, and False otherwise. An anagram is a word or phrase formed by rearranging the letters of another.

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

"""
"""
14.Simple, given a string of words, return the length of the shortest word(s).

def find_short(s):
    words = s.split()    
    min_length = min(len(word) for word in words)
    
    return min_length
"""
"""
15.Our football team has finished the championship.
Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.
For example: ["3:1", "2:2", "0:1", ...]
Points are awarded for each match as follows:
if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.
Notes:
our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4

def points(games):
    total_points = 0

    for match in games:
        x, y = map(int, match.split(":"))
        
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1

    return total_points

"""
"""
16.An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    string = string.lower()
    
    seen = set()
    
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    
    return True
"""
"""
17.Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

def sum_two_smallest_numbers(numbers):
    if len(numbers) < 4:
        return "Array should contain at least 4 positive integers."

    min_numbers = set()

    for num in numbers:
        if num > 0:
            min_numbers.add(num)

    if len(min_numbers) < 2:
        return "Array should contain at least 2 different positive integers."

    two_smallest = sorted(min_numbers)[:2]

    return sum(two_smallest)
"""
"""
18.Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    new_x = ''
    for digit in x:
        if int(digit) >= 5:
            new_x += '1'
        else:
            new_x += '0'
    return new_x
"""
"""
19.Code as fast as you can! You need to double the integer and return it.

def double_integer(i):
    total = (i*2);
    return total;
"""
"""
20.Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowelsCount = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in sentence:
        if char in vowels:
            vowelsCount += 1
    
    return vowelsCount
"""
"""
21.Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zeros = [num for num in nums if num != 0]
        zero_count = len(nums) - len(non_zeros)
        
        nums[:len(non_zeros)] = non_zeros
        nums[len(non_zeros):] = [0] * zero_count
"""
"""
22.ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
"""
"""
23.
An orderly trail of ants is marching across the park picnic area.
..ant..ant.ant...ant.ant..ant.ant....ant..ant.ant.ant...ant..
But suddenly there is a rumour that a dropped chicken sandwich has been spotted on the ground ahead. The ants surge forward! Oh No, it's an ant stampede!!
Some of the slower ants are trampled, and their poor little ant bodies are broken up into scattered bits.
The resulting carnage looks like this:
...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t
Can you find how many ants have died?

def dead_ant_count(ants):
    ants = ants.replace("ant", "")
    return max([ants.count("a"), ants.count("n"), ants.count("t")])
"""