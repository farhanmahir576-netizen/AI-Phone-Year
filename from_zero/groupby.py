def groupby(data):
    result = {}
    for key, value in data:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result

# Test
data = [("A", 10), ("B", 20), ("A", 30)]
print("Grouped:", groupby(data))  # Expected: {'A': [10, 30], 'B': [20]}
