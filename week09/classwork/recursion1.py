def factorial_recursive(n, values):
    # Base case: 1! = 1
    if n == 1:
        return 1
    product = n * factorial_recursive(n-1, values)   
    values[n] = product
    return product

values = {}
product = factorial_recursive(5, values)
print(f'{product=}')
print(f'{values=}')
# 5!

# 120
# return 5 * (return value) [24]
# return 4 * (return value) [6]
# return 3 * (return value) [2]
# return 2 * (return value) [1]
# return 1 {1200004}