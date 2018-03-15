import math


def primes():
    yield 2
    found_primes = [2]
    current_number = 3
    while True:
        for prime in found_primes:
            # we could speed this up by breaking here a using a found flag, but keep it simple
            if prime > math.sqrt(current_number):
                continue

            if current_number % prime == 0:
                break
        else:
            found_primes.append(current_number)
            yield current_number
        current_number += 1


if __name__ == "__main__":
    prim = primes()
    for i in range(100):
        print(next(prim))
