'''
# 1. Binary Search
def binary_search(arr, target):
    top, bot = 0, len(arr) - 1
    
    while top <= bot:
        mid = (top + bot) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            top = mid + 1
        else:
            bot = mid - 1
    
    return -1

# Test
print("1. Binary Search:", binary_search([1, 3, 5, 7, 9], 7))
---------------------------------------------------------------

# 2. Second Largest Number
def second_largest(arr):
    arr.sort()
    return arr[-2]

#or 

def find_second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements
    
    max1 = float('-inf')
    max2 = float('-inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    
    if max2 == float('-inf'):
        return None  # All elements are the same
    
    return max2

# Test
print("2. Second Largest:", second_largest([10, 5, 20, 8, 15]))
print("2. Second Largest (alt):", find_second_largest([12, 35, 1, 10, 34, 1]))
-------------------------------------------------------------------
# 3. Greatest Common Divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test
print("3. GCD:", gcd(48, 18))
-------------------------------------------------------------------

# 4. Perfect Number
def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    print("Sum of divisors:", sum)
    
    return sum == n

# Test
print("4. Perfect Number:", is_perfect(28))

-------------------------------------------------------------------
# 5. Frequency of Characters
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Test
print("5. Character Frequency:", char_frequency("konnichiwa"))
-------------------------------------------------------------------
#largest frequesnt element
from collections import Counter

def char_frequency(s):
    freq = Counter(s)
    max_char = freq.most_common(1)[0]
    return max_char

# Test
result = char_frequency("hello")
print(result)  # Output: ('l', 2)

#or
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Get character with maximum frequency
    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]

# Test
result = char_frequency("hello")
print(result)  # Output: ('l', 2)

#or

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Get character with maximum frequency
    max_char = max(freq.items(), key=lambda x: x[1])
    return max_char

# Test
result = char_frequency("hello")
print(result)  # Output: ('l', 2)

#or manual loop
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    max_char = ''
    max_count = 0
    for char, count in freq.items():
        if count > max_count:
            max_count = count
            max_char = char
    return (max_char, max_count)


# Test
result = char_frequency("mississippi")
print(result)  # Output: ('i', 4)

-------------------------------------------------------------------

# 6. Heap Sort
def heapify(arr, n, i):
    largest = i
    lc = 2 * i + 1
    rc = 2 * i + 2
    
    if lc < n and arr[lc] > arr[largest]:
        largest = lc
    if rc < n and arr[rc] > arr[largest]:
        largest = rc
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

# Test
print("6. Heap Sort:", heap_sort([12, 11, 13, 5, 6, 7]))



# 7. Non-Repeating Elements
def non_repeating(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    result = []
    for num in arr:
        if freq[num] == 1:
            result.append(num)
    return result

# Test
print("7. Non-Repeating:", non_repeating([1, 2, 3, 2, 4, 1, 5]))
#or
from collections import Counter

def non_repeating(arr):
    freq = Counter(arr)
    return [num for num in arr if freq[num] == 1]

# Test
print("7. Non-Repeating:", non_repeating([1, 2, 3, 2, 4, 1, 5]))
# Output: [3, 4, 5]
------------------------------------------------------------------------
# 8. Longest Palindrome in Array
def longest_palindrome_array(arr):
    def is_palindrome(s):
        return str(s) == str(s)[::-1]
    
    longest = ""
    for num in arr:
        s = str(num)
        if is_palindrome(s) and len(s) > len(longest):
            longest = s
    return longest

# Test
print("8. Longest Palindrome:", longest_palindrome_array([121, 1331, 12321, 45]))
-----------------------------------------------------------------

# 9. Add Two Matrices
def add_matrices(mat1, mat2):
    if len(mat1)!=len(mat2):
        return "error"
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

# Test
mat1 = [[1, 2, 3], [3, 4, 5]]
mat2 = [[5, 6, 3], [7, 8, 9]]
print("9. Add Matrices:", add_matrices(mat1, mat2))
--------------------------------------------------------------------------------------------

# 10. Check String Palindrome
def is_palindrome_string(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test
print("10. String Palindrome:", is_palindrome_string("racecar"))

#or using 2 pointers
def is_palindrome_string(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Test
print("10. String Palindrome (2 pointers):", is_palindrome_string("A man a plan a canal Panama"))
-----------------------------------------------------------------------------
# 11. Binary to Decimal
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        digit = binary % 10
        decimal += digit * (2 ** power)
        power += 1
        binary //= 10
    return decimal

# Test
print("11. Binary to Decimal:", binary_to_decimal(1010))
-------------------------------------------------------------------

# 12. Replace Substring
def replace_substring(string, old, new):
    return string.replace(old, new)

# Test
print("12. Replace Substring:", replace_substring("hello world", "world", "python"))

#or Replace Substring (Without using .replace())
def replace_substring(string, old, new):
    result = ""
    i = 0
    
    while i < len(string):
        # Check if substring matches at current position
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)  # Skip past the old substring
        else:
            result += string[i]
            i += 1
    
    return result

# Test
print("12. Replace Substring:", replace_substring("hello world", "world", "python"))

-------------------------------------------------------------------------------
# 13. Add Two Fractions
def add_fractions(n1, d1, n2, d2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    numerator = n1 * d2 + n2 * d1
    denominator = d1 * d2
    print(numerator,"/",denominator)
    g = gcd(numerator, denominator)
    return f"{numerator // g}/{denominator // g}"

# Test
print("13. Add Fractions:", add_fractions(1, 2, 1, 3))

'''
# 14. Prime Factors
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

# Test
print("14. Prime Factors:", prime_factors(60))
