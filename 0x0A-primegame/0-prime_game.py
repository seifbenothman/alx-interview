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

def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_count = [0] * (max_num + 1)

    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1]
        if i in primes:
            prime_count[i] += 1
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
