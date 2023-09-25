from functools import lru_chache

@lru_chache(maxsize = 11)
def fibonacci(n):
    if type(n) != int:
        print('Please try again')
    if type n < 1:
        print('Integer must be positive, please try again')

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
    for n in range(1, 11):
        print(n, ":", fibonacci(n))

fibonacci_cache = {}

@lru_cache(maxsize = 11)
def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    if n == 1:
        value = 1
    elif n == 2:
        value 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value

for n in range(1,11):
    print(n, ":", fibonacci(n))

    
