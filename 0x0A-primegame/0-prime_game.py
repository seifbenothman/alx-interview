#!/usr/bin/python3
def sieve_of_eratosthenes(max_num):
    """ Generate a list of primes up to max_num using the Sieve. """
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False
    p = 2
    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(max_num + 1) if is_prime[p]]


def optimal_play(primes, n):
    """ Determine if the player can make a move given the current state. """

    return any(prime <= n for prime in primes)


def isWinner(x, nums):
    """ Determine the winner of the prime game. """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_player = 'Maria'
        while True:
            if not optimal_play(primes, n):
                if current_player == 'Maria':
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            for prime in primes:
                if prime <= n:
                    n -= prime
                    n //= prime
                    break

            current_player = 'Ben' if current_player == 'Maria' else 'Maria'

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
