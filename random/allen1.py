def find_allens_value(N, A, G):
    min_value = float('inf')
    
    # Try removing each pair of elements from A
    for i in range(N):
        for j in range(i + 1, N):
            # Get remaining elements after removing indices i and j
            remaining = [A[k] for k in range(N) if k != i and k != j]
            
            # Sort both arrays
            remaining_sorted = sorted(remaining)
            G_sorted = sorted(G)
            
            # Calculate the added value
            x = G_sorted[0] - remaining_sorted[0]
            
            # Check if this x works for all elements
            if all(remaining_sorted[k] + x == G_sorted[k] for k in range(len(remaining_sorted))) and x > 0:
                min_value = min(min_value, x)
    
    return min_value


# Test with your example
N = 3
A = [2, 1, 3]
G = [2]

result = find_allens_value(N, A, G)
print(f"Input: N={N}, A={A}, G={G}")
print(f"Minimum value Allen added: {result}")