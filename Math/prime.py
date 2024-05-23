def is_prime(n):
    if n < 2:
        return False

    if n in (2, 3):
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# n이하 소수의 리스트 반환
def make_prime_sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [x for x in range(2, n + 1) if primes[x]]
