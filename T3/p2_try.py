import io
import os
import sys
import math as mt
import time
from collections import Counter

"""
https://math.stackexchange.com/questions/621109/co-prime-numbers-less-than-n
https://en.wikipedia.org/wiki/Euler%27s_totient_function
https://codinglab.huostravelblog.com/math/coprime-finder/index.php
https://www.hackmath.net/en/calculator/n-choose-k?n=48&k=13&order=0&repeat=0
https://en.wikipedia.org/wiki/Modular_arithmetic



Harmonic Progression of the sum of primes
https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn/


Mini hint para la dos, se puede calcular la cantidad de números coprimos con n sin encontrar 
explícitamente los números que son coprimos con n. Lo otro, recuerden que literalmente estamos pidiendo
 el dígito menos significativo que no es cero. Yo diría que algo así como el 90% de la dificultad es darse
  cuenta de cómo encontrar ese dígito sin hacer todos los cálculos explícitos, porque spoiler no hay forma
   que logren hacer todos esos cálculos explícitos en el tiempo dado.


Creo que voy a dar tres mini hints, 

la criba de erastostenes puede ser usada para factorizar en O(log(n))
 (o directamente pueden usarla para calcular phi(n) para todo n y encontrar primos al mismo tiempo), dado
  la factorización de n, 

  phi(n) se puede calcular en O(log(n)) 

  y por último se puede conseguir la factorización de n! en O(n).


https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/

https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/?ref=lbp

https://www.geeksforgeeks.org/optimized-euler-totient-function-multiple-evaluations/

"""

# a, b = list(map(int, sys.stdin.readline().strip().split()))
# Sieve: O(nloglogn)

MAX = 100001
MAXN = 100001

# SPF (Smallest Prime Factor)
spf = [0 for i in range(MAXN)]


# Time Complexity : O(nloglogn)


def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i

    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
        if spf[i] == i:
            for j in range(i * i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i


# A O(log n) function returning prime
# factorization by dividing by smallest
# prime factor at every step
def getFactorization(x):
    initial = x
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]

    print("Factorization of ", initial, "is", ret)
    return ret


# No of Factors of n!
def number_of_factors_of_n_factorial(n, p):
    if p == 1:
        return 0
    x = p
    exponent = 0
    while n // x > 0:
        exponent += n // x
        x *= p
    return exponent


# A O(log n) function returning prime
# factorization by dividing by smallest
# prime factor at every step
def get_factorization(x):
    initial = x
    ret = list()
    while x != 1:
        ret.append(sieve_of_erathosthenes[x])
        x = x // sieve_of_erathosthenes[x]

    print("Factorization of ", initial, "is", ret)
    return ret


def get_least_sig_digit(full_number):
    full_number = str(full_number)
    reversed_number = full_number[::-1]
    pos = 0
    digit = reversed_number[pos]
    while digit == "0":
        pos += 1
        digit = reversed_number[pos]
    return digit


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


def total_subgroups(n, k):
    if k > n:
        return -1
    print("-----------------------------\nn:", n, "k:", k, "\n-----------------------------")

    # sieve erastostenes factorizar en O(log(n))
    sieve()

    # print("sieve",  spf)

    # phi(n) - O(log(n))
    total_coprimes = phi(n)
    # print("total_coprimes: ", total_coprimes)
    total_combinations = 0
    ans = 1

    """

    n_fact = mt.factorial(total_coprimes)
    k_fact = mt.factorial(k)
    n_k_fact = mt.factorial(total_coprimes-k)
    factorization = getFactorization(n_fact)
    factorization_2 = getFactorization(k_fact)
    factorization_3 = getFactorization(n_k_fact)

    denom = list((Counter(factorization_2) + Counter(factorization_3)).elements())
    total = list((Counter(factorization) - Counter(denom)).elements())

    res = 1
    for i in total:
        res *= i

    """

    # n! factorization - O(n)

    """
    for p in range(1, n):
        #print(p, sieve_of_erathosthenes[p])
        if sieve_of_erathosthenes[p] == p:
            ans *= (number_of_factors_of_n_factorial(n, p) + 1)
    """

    print("ans", ans)
    print("n Chooses k: ", total_combinations)

    if total_combinations == 0:
        return -1

    else:
        least_significant_digit = get_least_sig_digit(total_combinations)
        print("Least Significant Non Zero Bit: ", least_significant_digit)
        return least_significant_digit


range_input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
upper_bound, subset_size = list(map(int, range_input().decode().strip().split()))
result = total_subgroups(upper_bound, subset_size)
print("RESULT: ", str(result))
# sys.stdout.write(str(result))





