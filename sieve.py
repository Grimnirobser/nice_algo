def sieve(n):
    """
    sieve of Eratosthenes, O(n log log n).
    """
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

def euler_sieve(n):
    """
    Euler sieve, O(n).
    """
    primes = []
    is_prime = [True]*n
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if p * i >= n:
                break
            is_prime[p*i] = False
            if i % p == 0:
                break
    return primes
    


print(euler_sieve(100))
