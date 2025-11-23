'''
# 15. Convert Digits to Words
def digits_to_words(n):
    words = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    
    result = []
    for digit in str(n):
        result.append(words[digit])
    
    return ' '.join(result)

# Test
print("15. Digits to Words:", digits_to_words(1234))
---------------------------------------------------------------------------------

# 16. String Match with Wildcard
#What is Wildcard Matching?
#Match a string with a pattern that contains:

#   * → Matches zero or more characters
#   ? → Matches exactly one character
'''
def wildcard_match(string, pattern):
    i = 0
    j = 0
    
    while i < len(string) and j < len(pattern):
        if pattern[j] == '*':
            # Match zero or more characters
            if j == len(pattern) - 1:
                return True
            j += 1
            while i < len(string) and string[i] != pattern[j]:
                i += 1
        elif pattern[j] == '?' or pattern[j] == string[i]:
            # Match single character
            i += 1
            j += 1
        else:
            return False
    
    return i == len(string) and j == len(pattern)

# Test
print("16. Wildcard Match:", wildcard_match("hello", "h*o"))
print("16. Wildcard Match:", wildcard_match("hello", "h?llo"))
'''
---------------------------------------------------------------------------------

# 17. Spiral Traversal of Matrix
def spiral_traversal(matrix):
    if not matrix:
        return []
    
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

# Test
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("17. Spiral Traversal:", spiral_traversal(matrix))
---------------------------------------------------------------------------

# 18. Find Prime Pairs (p*q <= n)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_pairs(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    
    pairs = []
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] * primes[j] <= n:
                pairs.append((primes[i], primes[j]))
            else:
                break
    
    return pairs

# Test
print("18. Prime Pairs (n=30):", find_prime_pairs(30))
------------------------------------------------------------------------------------

# 19. Roman to Integer
def roman_to_integer(s):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_values[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total

# Test
print("19. Roman to Integer (XIV):", roman_to_integer("XIV"))
print("19. Roman to Integer (MCMXC):", roman_to_integer("MCMXC"))
-----------------------------------------------------------------------

# 20. Check if Four Points Form a Square
def distance_squared(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def is_square(points):
    if len(points) != 4:
        return False
    
    # Calculate all 6 distances between 4 points
    distances = []
    for i in range(4):
        for j in range(i + 1, 4):
            distances.append(distance_squared(points[i], points[j]))
    
    distances.sort()
    
    # A square has 4 equal sides and 2 equal diagonals
    # After sorting: first 4 should be sides, last 2 should be diagonals
    if (distances[0] == distances[1] == distances[2] == distances[3] and
        distances[4] == distances[5] and
        distances[4] == 2 * distances[0]):
        return True
    
    return False

# Test
points1 = [(0, 0), (0, 1), (1, 1), (1, 0)]
points2 = [(0, 0), (1, 1), (2, 0), (1, -1)]
points3 = [(0, 0), (2, 0), (0, 2), (2, 2)]

print("20. Is Square (square):", is_square(points1))
print("20. Is Square (diamond):", is_square(points2))
print("20. Is Square (square):", is_square(points3))
'''