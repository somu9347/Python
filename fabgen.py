def fibonacci(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)
