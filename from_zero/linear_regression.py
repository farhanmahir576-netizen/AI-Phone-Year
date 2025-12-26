def mean(nums):
    return sum(nums) / len(nums)

class LinearRegression1D:
    def __init__(self):
        self.m = 0
        self.b = 0

    def fit(self, x, y):
        x_mean = mean(x)
        y_mean = mean(y)
        numerator = sum((xi - x_mean)*(yi - y_mean) for xi, yi in zip(x, y))
        denominator = sum((xi - x_mean)**2 for xi in x)
        self.m = numerator / denominator
        self.b = y_mean - self.m * x_mean

    def predict(self, x):
        return [self.m * xi + self.b for xi in x]

# Test
x_train = [1, 2, 3, 4, 5]
y_train = [2, 4, 6, 8, 10]

model = LinearRegression1D()
model.fit(x_train, y_train)
print("Predictions:", model.predict([6, 7]))  # Expected: [12, 14]
