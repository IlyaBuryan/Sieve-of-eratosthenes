"""
Позволяет эффективно найти необходимое по счету (№N) простое число.
Allows to effectively find an №N prime number
"""


def erat_fun(n):
    """With Sieve-of-eratosthenes"""
    prime = [2]
    i = 3
    while len(prime) < n:
        if all(map(lambda k: i % k != 0, prime)):
            prime.append(i)
        i += 1
    return prime[-1]
