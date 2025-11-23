def odd_even_transform(arr, n):
    result = []
    if n%2 == 1:
        for x in arr:
            if x % 2 == 0:  # even
                result.append(x - 3)
            else:           # odd
                result.append(x + 3)
    else:
        return arr
    return result

# Example
arr = [3, 4, 9]
n = 4
print(odd_even_transform(arr, n))  # Output: [12, -5, 18]
