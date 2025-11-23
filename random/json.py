import json

def getSONDiff(json1, json2):
    # Convert JSON strings to Python dictionaries
    dict1 = json.loads(json1)
    dict2 = json.loads(json2)
    
    # Find common keys
    common_keys = set(dict1.keys()) & set(dict2.keys())
    
    # Collect keys where values differ
    diff_keys = [key for key in common_keys if dict1[key] != dict2[key]]
    
    # Return sorted list
    return sorted(diff_keys)

# Example usage:
json1 = '{"hello":"world","hi":"hello","you":"me"}'
json2 = '{"hello":"world","hi":"hello!","you":"me"}'

print(getSONDiff(json1, json2))
