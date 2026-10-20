def factorial(N):
    """
    Compute the factorial of N. If N <= 10, use a fast lookup table;
    otherwise use scipy.special.factorial.
    """
    if N < len(FACTORIALS):
        return FACTORIALS[N]
    else:
        from scipy import special
        return int(special.factorial(N))
