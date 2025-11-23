# code to count the number of triplets in an array whose sum is divisible by a given integer d
def count_divisible_triplets(arr, d):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) % d == 0:
                    count += 1
    return count


# Example usage
arr = [3, 3, 4, 7, 8]
d = 5
print("Number of triplets:", count_divisible_triplets(arr, d))
# Output should be 4

#or 

from collections import Counter

def count_divisible_triplets(arr, d):
    # Step 1: Count occurrences of each remainder
    remainder_count = Counter([x % d for x in arr])
    count = 0

    # Step 2: Iterate combinations of remainders (r1 <= r2 <= r3)
    remainders = list(remainder_count.keys())

    for i, r1 in enumerate(remainders):
        for j, r2 in enumerate(remainders[i:], start=i):
            # Find r3 such that (r1 + r2 + r3) % d == 0
            r3 = (-r1 - r2) % d
            if r3 not in remainder_count:
                continue

            c1, c2, c3 = remainder_count[r1], remainder_count[r2], remainder_count[r3]

            # Handle cases (all same, two same, all different)
            if r1 == r2 == r3:
                count += c1 * (c1 - 1) * (c1 - 2) // 6  # nC3
            elif r1 == r2 != r3:
                count += (c1 * (c1 - 1) // 2) * c3     # nC2 * c3
            elif r1 < r2 < r3:  # ensure distinct and count once
                count += c1 * c2 * c3

    return count


# Example usage
arr = [3, 3, 4, 7, 8]
d = 5
print("Number of triplets:", count_divisible_triplets(arr, d))
