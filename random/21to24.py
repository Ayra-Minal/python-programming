'''
# 21. Calculate Day of the Week for Any Date
def day_of_week(day, month, year):
    # Zeller's Congruence Algorithm
    if month < 3:
        month += 12
        year -= 1
    
    q = day
    m = month
    k = year % 100
    j = year // 100
    
    h = (q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return days[h]

# Test
print("21. Day of Week (4/5/2004):", day_of_week(15, 8, 1947))
print("21. Day of Week (23/10/2025):", day_of_week(1, 1, 2025))


from datetime import datetime

def day_of_week(day, month, year):
    
    date_obj = datetime(year, month, day)
    return date_obj.strftime("%A")

# Test examples
print("21. Day of Week (4/5/2004):", day_of_week(4, 5, 2004))
print("21. Day of Week (1/1/2025):", day_of_week(1, 1, 2025))

----------------------------------------------------------------------


# 22. Count Number of Squares in m x n Matrix
def count_squares(m, n):
    total = 0
    
    # For each possible square size
    for size in range(1, min(m, n) + 1):
        # Count how many squares of this size fit
        rows = m - size + 1
        cols = n - size + 1
        total += rows * cols
    
    return total

# Test
print("22. Count Squares (3x3 matrix):", count_squares(3, 3))
print("22. Count Squares (4x3 matrix):", count_squares(4, 3))


------------------------------------------------------------------------
# 23. Chocolate Distribution Problem
def distribute_chocolates(chocolates, m):
    n = len(chocolates)
    
    # Not enough packets
    if m > n:
        return -1
    
    # Sort the array
    chocolates.sort()
    
    min_diff = float('inf')
    
    # Find minimum difference window of size m
    for i in range(n - m + 1):#number of windows 
        diff = chocolates[i + m - 1] - chocolates[i]
        min_diff = min(min_diff, diff)
    
    return min_diff

# Test
chocolates1 = [7, 3, 2, 4, 9, 12, 56]
m1 = 3
print("23. Chocolate Distribution:", distribute_chocolates(chocolates1, m1))

chocolates2 = [3, 4, 1, 9, 56, 7, 9, 12]
m2 = 5
print("23. Chocolate Distribution:", distribute_chocolates(chocolates2, m2))
---------------------------------------------------------------------------
'''
# 24. Nuts and Bolts Matching Problem
def match_nuts_bolts(nuts, bolts):
    
    order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']
    
    # Create a dictionary for quick lookup
    order_map = {char: i for i, char in enumerate(order)}
    
    # Sort nuts based on the order
    nuts.sort(key=lambda x: order_map[x])
    
    # Sort bolts based on the order
    bolts.sort(key=lambda x: order_map[x])
    
    return nuts, bolts

# Test
nuts = ['@', '%', '$', '#', '^']
bolts = ['%', '@', '#', '$', '^']

matched_nuts, matched_bolts = match_nuts_bolts(nuts, bolts)
print("24. Nuts and Bolts Matching:")
print("   Nuts:", matched_nuts)
print("   Bolts:", matched_bolts)

# Another test
nuts2 = ['*', '&', '?', '#', '@']
bolts2 = ['#', '&', '*', '@', '?']

matched_nuts2, matched_bolts2 = match_nuts_bolts(nuts2, bolts2)
print("24. Nuts and Bolts Matching:")
print("   Nuts:", matched_nuts2)
print("   Bolts:", matched_bolts2)
