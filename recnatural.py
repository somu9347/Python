def sum_natural(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    return n + sum_natural(n - 1)

print(sum_natural(30))
       