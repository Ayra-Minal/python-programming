'''
# In a toy shop there are a number of toys presented with several various – 
# priced toys in a specific order. You have a limited budget and would like 
# to select the greatest number of consecutive toys that fit within the budget.
# Given prices of the toys and your budget, 
# what is the maximum number of toys that can be purchased for your child?


def getmaxtoys(prices, money):
    start=0
    current_sum=0
    max_toys=0
    
    for i in range(len(prices)):
        current_sum+=prices[i]
        while current_sum>money:
            current_sum-=prices[start]
            start+=1
        max_toys=max(max_toys,i-start+1)
    return max_toys
# Test
prices = [1,4,5,3,2,1,6]
money = 6
print("Max Toys:", getmaxtoys(prices, money))

----------------------------------------------------------------------------

# Function to check if a number is a stepping number
def is_stepping(num):
    s = str(num)
    for i in range(1, len(s)):
        # Check if difference between adjacent digits is exactly 1
        if abs(int(s[i]) - int(s[i - 1])) != 1:
            return False
    return True


# Function to display all stepping numbers in the given range
def displaySteppingNumbers(n, m):
    for num in range(n, m + 1):
        if is_stepping(num):
            print(num, end=' ')


# --- Main Program ---
n = 0
m = 100
print("Stepping Numbers between", n, "and", m, ": ")
displaySteppingNumbers(n, m)

----------------------------------------------------------------------------

# 24. Minimize Ticket Price by Removing k Digits
def minimize_ticket_price(ticket, k):
    stack = []

    for digit in ticket:
        # Remove larger digits from the stack if possible
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # If k still > 0, remove remaining digits from the end
    while k > 0:
        stack.pop()
        k -= 1

    # Convert stack to string
    result = ''.join(stack).lstrip('0')  # remove leading zeros

    # If result is empty, return "0" (cannot make cost zero but can have a single zero)
    return result if result != '' else '0'

# Test
ticket = "1432219"
k = 3   # Example: 2

print(minimize_ticket_price(ticket, k))

---------------------------------------------------------------------------
# 24. Weight Machine Problem
def weightMachine(N, weights, T):
    total_amount = 0  # total fare to be paid

    for w in weights:
        if w > T:        # if luggage exceeds threshold
            total_amount += 2  # pay double fare
        else:
            total_amount += 1  # pay base fare

    return total_amount


# ---- Sample Test ----
# number of luggage
N = 4
# weights of each luggage
weights = [1, 2, 3, 4]
# threshold weight
T = 3

# calling the function
result = weightMachine(N, weights, T)
print("Total amount to be paid:", result)

---------------------------------------------------------------------------
# 25. Majority Element in an Array
from collections import Counter

def findMajorityElement(arr):
    n = len(arr)
    counts = Counter(arr)
    
    # Get the element with the highest frequency
    max_element, max_count = counts.most_common(1)[0]

    # Check if it occurs more than n//2 times
    if max_count > n // 2:
        return max_element
    else:
        return "No majority element"


# ---- Sample Test ----
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print("Majority Element:", findMajorityElement(arr))
---------------------------------------------------------------------------

# 26. Maximum Loss Problem
def max_loss(prices):
    if not prices or len(prices) < 2:
        return 0

    max_price = prices[0]  # highest price seen so far
    max_loss_val = 0       # maximum loss encountered

    for price in prices[1:]:
        loss = max_price - price  # loss if bought at max_price and sold today
        max_loss_val = max(max_loss_val, loss)
        max_price = max(max_price, price)  # update max_price if current price is higher

    return max_loss_val


# ---- Sample Test ----
prices = [1, 8, 4, 2, 10, 3, 2]
print("Maximum Loss:", max_loss(prices))

---------------------------------------------------------------------------

# 27. Brainwashed Avengers Problem
def brainwashed_avengers(powers):
    powers.sort(reverse=True)  # sort descending
    total_power = sum(powers)
    brainwashed_power = 0
    count = 0

    for p in powers:
        brainwashed_power += p
        total_power -= p  # remaining sum
        count += 1
        if brainwashed_power > total_power:
            break

    return count


# ---- Sample Test ----
powers = [9, 3, 1, 2, 4, 2]
print(brainwashed_avengers(powers))

---------------------------------------------------------------------------

# 28. Hostel Room Allocation Problem
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def hostel_order(students):
    prime_chars = []
    composite_chars = []

    for ch in students:
        ascii_val = ord(ch)
        if is_prime(ascii_val):
            prime_chars.append(ch)
        else:
            composite_chars.append(ch)

    # Sort prime_chars in ascending order
    prime_chars.sort(key=lambda x: ord(x))

    # Sort composite_chars in descending order
    composite_chars.sort(key=lambda x: ord(x), reverse=True)

    # Combine prime first, then composite
    return ''.join(prime_chars + composite_chars)

# Sample Input
students = "Kkunjkhahorin"
print(hostel_order(students))

---------------------------------------------------------------------------

#employee have special numbers of length m with digits from 0-9
#digits in non decreasing order...find total special numbers for given m values
from math import comb  # Python 3.8+ (for combinations)

def special_numbers(n, arr):
    total = 0
    for m in arr:
        total += comb(10 + m - 1, m)  # non-decreasing sequences formula
    return total


# ---- Sample Test ----
n = 2
arr = [4, 1]
print(special_numbers(n, arr))

---------------------------------------------------------------------------

# 30. Kth Good Prime Problem
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits(num):
    return sum(int(d) for d in str(num))

def kth_good_prime(N, K):
    count = 0
    current = N + 1
    
    while True:
        if is_prime(current):
            if is_prime(sum_of_digits(current)):
                count += 1
                if count == K:
                    return current
        current += 1


# ---- Sample Test ----
N, K = 4, 4
print(kth_good_prime(N, K))  # Output: 12

N, K = 17, 5
print(kth_good_prime(N, K))  # Output: 29
'''