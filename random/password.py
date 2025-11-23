def min_flips_to_secure_password(pwd):
    flips = 0
    for i in range(0, len(pwd), 2):
        # ensure we have a complete pair
        if i + 1 < len(pwd):
            if pwd[i] != pwd[i + 1]:
                flips += 1
    return flips

# Example usage
pwd = "0101101101"
print("Minimum flips needed:", min_flips_to_secure_password(pwd))
#output = 3