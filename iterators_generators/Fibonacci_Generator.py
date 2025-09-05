def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

# Use generator
for num in fibonacci(7):
    print(num)
