import io
import os
import sys
from collections import Counter

"""
https://math.stackexchange.com/questions/621109/co-prime-numbers-less-than-n
https://en.wikipedia.org/wiki/Euler%27s_totient_function
https://codinglab.huostravelblog.com/math/coprime-finder/index.php
https://www.hackmath.net/en/calculator/n-choose-k?n=48&k=13&order=0&repeat=0
https://en.wikipedia.org/wiki/Modular_arithmetic

Harmonic Progression of the sum of primes
https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn/

https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/

https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/?ref=lbp

https://www.geeksforgeeks.org/optimized-euler-totient-function-multiple-evaluations/
"""

# Sieve: O(nloglogn)

MAX = 1000001
all_primes = []


def sieve():
    is_prime_number = [0] * (MAX + 1)
    for i in range(2, MAX + 1):
        if is_prime_number[i] == 0:
            all_primes.append(i)
            j = 2
            while i * j <= MAX:
                is_prime_number[i * j] = 1
                j += 1


def phi(n):
    res = n
    i = 0
    while all_primes[i] * all_primes[i] <= n:
        if n % all_primes[i] == 0:
            res -= int(res / all_primes[i])
            while n % all_primes[i] == 0:
                n = int(n / all_primes[i])
        i += 1

    if n > 1:
        res -= int(res / n)

    return res


def prime_factorization(n):
    result = {}

    for p in all_primes:
        if p < n + 1:
            e = 0
            m = n // p
            while m:
                e += m
                m //= p

            result[p] = e
        else:
            break

    return result


def total_subgroups(n, k):
    if k > n:
        return -1

    # sieve erasthosthenes factorizar en O(log(n))
    sieve()

    total_coprimes = phi(n)
    # print("total_coprimes: ", total_coprimes)

    # n! factorization - O(n)
    coprimes_fact = prime_factorization(total_coprimes)
    # print("numerador: ", coprimes_fact)

    k_fact = prime_factorization(k)
    # print("k_fact: ", k_fact)
    k_n_fact = prime_factorization(total_coprimes-k)
    # print("k_n_fact: ", k_n_fact)

    for key, val in k_n_fact.items():
        if key in k_fact:
            k_fact[key] += val
        else:
            k_fact[key] = val

    for key, val in k_fact.items():
        if key in coprimes_fact:
            coprimes_fact[key] -= val
        else:
            coprimes_fact[key] = -val

    # print("denominador: ", k_fact)

    # print("Factorizacion final", coprimes_fact)

    if 2 in coprimes_fact and 5 in coprimes_fact:
        min_exp = min(coprimes_fact[2], coprimes_fact[5])
        coprimes_fact[2] -= min_exp
        coprimes_fact[5] -= min_exp

    # print("Despues de eliminar 2s con 5s", coprimes_fact)

    resultado = 1
    for key, value in coprimes_fact.items():
        if key == 2 and value < 0:
            resultado = (resultado * pow(5, -value, 10)) % 10

        elif key == 5 and value < 0:
            resultado = (resultado * pow(2, -value, 10)) % 10

        else:
            resultado = (resultado * pow(key, value, 10)) % 10

    if resultado == 0:
        return -1

    else:
        return resultado


range_input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
upper_bound, subset_size = list(map(int, range_input().decode().strip().split()))
result = total_subgroups(upper_bound, subset_size)
sys.stdout.write(str(result))
