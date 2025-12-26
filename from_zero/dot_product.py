def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Lists must be of the same length")
    return sum(a[i] * b[i] for i in range(len(a)))

# Test
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]
print("Dot Product:", dot_product(vec1, vec2))  # Expected: 32
