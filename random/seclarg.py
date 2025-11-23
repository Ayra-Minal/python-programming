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


arr = [12, 35, 1, 10, 34, 1]
print(find_second_largest(arr))  # Output: 34

