def recursive_fib(n):
    """F(n) = F(n-1) + F(n-2) F(0) = 0, F(1) = 1
    Time Complexity: O(F(n))
    """
    if n <= 1:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)