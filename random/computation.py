
def min_operations_to_make_odd(computationalTime):
    operations = 0
    
    # Loop until all elements in the array are odd
    while any(x % 2 == 0 for x in computationalTime):
        # Find the maximum even computational time
        c = max(x for x in computationalTime if x % 2 == 0)
        
        # Apply the operation: halve all elements that are even and equal to c
        computationalTime = [x // 2 if x == c else x for x in computationalTime]
        
        # Increment operation count
        operations += 1
    
    return operations

# Example usage:
computationalTime = [2, 8, 16]
print(min_operations_to_make_odd(computationalTime))  # Output should be 4
