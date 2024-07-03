#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Return a list of primes up to n (inclusive) using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]

def count_prime_moves(n, primes):
    """Return the number of moves that can be made with the primes up to n."""
    count = 0
    for prime in primes:
        if prime <= n:
            count += 1
        else:
            break
    return count

def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        prime_moves = count_prime_moves(n, primes)
        if prime_moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Ensure the file ends with a new line
