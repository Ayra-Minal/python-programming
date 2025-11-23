def find_minimum_moves(word):
    moves = 0
    freq = {}

    # Count frequency of each character
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1

    # For each character, every pair can be removed in one move
    for count in freq.values():
        moves += count // 2

    return moves


# Example usage
word = "baabacaa"
print("Minimum moves:", find_minimum_moves(word))
