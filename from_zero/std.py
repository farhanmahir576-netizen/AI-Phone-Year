import math

def mean(nums):
    return sum(nums) / len(nums)

def std(nums):
    m = mean(nums)
    variance = sum((x - m) ** 2 for x in nums) / len(nums)
    return math.sqrt(variance)

# Test
numbers = [10, 20, 30, 40]
print("Standard Deviation:", std(numbers))  # Expected ~11.1803
