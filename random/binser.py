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
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    target = 7
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")
