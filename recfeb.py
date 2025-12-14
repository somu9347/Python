#Definition:
#F(n) = F(n−1) + F(n−2)
#F(0) = 0, F(1) = 1

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(45))

