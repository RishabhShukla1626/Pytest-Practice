def fibonacci_naive(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


cache = {}

def fibonacci_cached(n):
    if n in cache:
        return cache[n]
    if n==0 or n==1:
        return n
    fn = fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
    cache[n] = fn
    return fn