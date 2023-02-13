from timeit import default_timer as timer
from typing import Union, Tuple
from gmpy2 import mpz, isqrt, is_square


def fermat(n: Union[int, str, mpz]) -> Tuple[mpz, mpz]:
    n_mpz = mpz(n)  # coerce into mpz
    t = isqrt(n_mpz) + 1  # isqrt is the floor, add 1 to get ceiling
    while not is_square(t ** 2 - n_mpz):  # while t^2 - n is not a perfect square
        t += 1  # add 1 to t
    #  at this point we have found a perfect square so get the sqrt for final results
    s = isqrt(t ** 2 - n_mpz)
    p = t + s
    q = t - s
    return p, q


if __name__ == '__main__':
    # n = 121607 * 74731  # product of two random 16-bit prime integers

    # The following completes in about 30 sec on an Apple M1
    n = 8392559569 * 4322277823  # product of two random 32-bit prime integers

    # Assuming about ~10,400,000 integers / sec calculation the next 128-bit n would take ~13,284,055,518 sec or 421 years
    # n = 15391574578848764431 * 11543409319038274373  # product of two random 64-bit prime integers

    start = timer()
    print(fermat(n))
    end = timer()

    print(f"Time taken in seconds: {end - start}")  # Time in seconds,
