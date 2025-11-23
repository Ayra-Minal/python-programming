# ========================================================================
# 1. ADD TWO NUMBERS
# ========================================================================
# You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order, and each of their 
# nodes contains a single digit. Add the two numbers and return the sum 
# as a linked list.
# Example: Input: l1 = [2,4,3], l2 = [5,6,4]  Output: [7,0,8]
# ========================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    return dummy.next

print("1. ADD TWO NUMBERS")
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = addTwoNumbers(l1, l2)
output = []
while result:
    output.append(result.val)
    result = result.next
print(f"   [2,4,3] + [5,6,4] = {output}")
print()


# ========================================================================
# 2. TOP K FREQUENT WORDS
# ========================================================================
# Given an array of strings words and an integer k, return the k most 
# frequent strings. Return the answer sorted by the frequency from 
# highest to lowest. Sort the words with the same frequency by their 
# lexicographical order.
# Example: Input: words = ["i","love","leetcode","i","love","coding"], k = 2
#          Output: ["i","love"]
# ========================================================================

from collections import Counter
import heapq

def topKFrequent(words, k):
    count = Counter(words)
    return heapq.nsmallest(k, count.keys(), key=lambda x: (-count[x], x))

print("2. TOP K FREQUENT WORDS")
print(f"   Input: ['i','love','leetcode','i','love','coding'], k=2")
print(f"   Output: {topKFrequent(['i','love','leetcode','i','love','coding'], 2)}")
print()


# ========================================================================
# 3. FIZZ BUZZ
# ========================================================================
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
# Example: Input: n = 15  Output: ["1","2","Fizz","4","Buzz",...]
# ========================================================================

def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print("3. FIZZ BUZZ")
print(f"   Input: n=15")
print(f"   Output: {fizzBuzz(15)}")
print()


# ========================================================================
# 4. VALID PARENTHESES
# ========================================================================
# Given a string s containing just the characters '(', ')', '{', '}', 
# '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# Example: Input: s = "()[]{}"  Output: true
# ========================================================================

def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return not stack

print("4. VALID PARENTHESES")
print(f"   Input: '()[]{{}}' → Output: {isValid('()[]{}')} ")
print(f"   Input: '([)]'   → Output: {isValid('([)]')}")
print()


# ========================================================================
# 5. CANDY
# ========================================================================
# There are n children standing in a line. Each child is assigned a 
# rating value given in the integer array ratings. You are giving 
# candies to these children subjected to the following requirements:
# 1. Each child must have at least one candy.
# 2. Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute.
# Example: Input: ratings = [1,0,2]  Output: 5
# ========================================================================

def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)

print("5. CANDY")
print(f"   Input: ratings=[1,0,2] → Output: {candy([1,0,2])} candies")
print(f"   Input: ratings=[1,2,2] → Output: {candy([1,2,2])} candies")
print()


# ========================================================================
# 6. FIRST MISSING POSITIVE
# ========================================================================
# Given an unsorted integer array nums, return the smallest missing 
# positive integer. You must implement an algorithm that runs in O(n) 
# time and uses O(1) auxiliary space.
# Example: Input: nums = [3,4,-1,1]  Output: 2
# ========================================================================

def firstMissingPositive(nums):
    n = len(nums)
    
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1

print("6. FIRST MISSING POSITIVE")
print(f"   Input: [3,4,-1,1] → Output: {firstMissingPositive([3,4,-1,1])}")
print(f"   Input: [7,8,9,11,12] → Output: {firstMissingPositive([7,8,9,11,12])}")
print()


# ========================================================================
# 7. REVERSE INTEGER
# ========================================================================
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit 
# integer range [-2^31, 2^31 - 1], then return 0.
# Example: Input: x = 123  Output: 321
# ========================================================================

def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    result = 0
    
    while x:
        result = result * 10 + x % 10
        x //= 10
    
    result *= sign
    
    if result < -2**31 or result > 2**31 - 1:
        return 0
    
    return result

print("7. REVERSE INTEGER")
print(f"   Input: x=123  → Output: {reverse(123)}")
print(f"   Input: x=-123 → Output: {reverse(-123)}")
print(f"   Input: x=120  → Output: {reverse(120)}")