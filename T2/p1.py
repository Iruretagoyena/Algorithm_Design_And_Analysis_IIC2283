import sys
import math
import cmath
import io
import os

"""
size_s, size_t, k = list(map(int, sys.stdin.readline().strip().split()))
s_word = sys.stdin.readline().strip()
t_word = sys.stdin.readline().strip()
# t_word_reversed = t_word[::-1]

"""

input_ = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

size_s, size_t, k = list(map(int, input_().decode().strip().split()))
s_word = input_().decode().strip()
t_word = input_().decode().strip()
# t_word_reversed = t_word[::-1]

pow_2 = dict()


def fast_fourier_transform(polynomial, size_polynomial):
    """
    Two-point DFT (N=2) => A0 = a0 + a1, A1 = a0 − a1
    Si quedan 2 elementos => Ultima iteracion de descomposicion
    """
    if size_polynomial == 2:
        first = polynomial[0]
        second = polynomial[1]
        return [first + second, first - second]
    """
    2+ point DFT (N>=2) 
    Si no, seguir resolviendo
    """
    curr_result_fft = [0]*size_polynomial

    # Separar y resolver los index pares
    even_polinomial_idxs = polynomial[: size_polynomial: 2]
    len_even_polinomial_idxs = len(even_polinomial_idxs)
    solve_evens = fast_fourier_transform(even_polinomial_idxs, len_even_polinomial_idxs)

    # Separar y resolver los index impares
    odd_polinomial_idxs = polynomial[1: size_polynomial: 2]
    len_odd_polinomial_idxs = len(odd_polinomial_idxs)
    solve_odds = fast_fourier_transform(odd_polinomial_idxs, len_odd_polinomial_idxs)

    mid_point = size_polynomial // 2
    for position in range(mid_point):
        even_at_pos = solve_evens[position]
        odd_at_pos = solve_odds[position]
        pow_2_at_pos = pow_2[size_polynomial][position]
        odd_times_pow = pow_2_at_pos * odd_at_pos
        curr_result_fft[position] = even_at_pos + odd_times_pow
        curr_result_fft[mid_point + position] = even_at_pos - odd_times_pow

    return curr_result_fft


size_of_pow = max(size_s, size_t)
pow_size = 2 ** math.ceil(math.log2(size_of_pow))
# Butterflies and Bit-Reversal
result_aggregator_array = [0] * pow_size

precalculate = pow_size
precalculate_pi = cmath.pi * 2j

while precalculate > 0:
    powers_of_n = dict()
    for k_value in range(0, precalculate // 2):
        power = cmath.exp(precalculate_pi * k_value / precalculate)
        powers_of_n[k_value] = power

    pow_2[precalculate] = powers_of_n
    precalculate = precalculate // 2

alphabet = "ATGC"
for solve_letter in alphabet:
    binary_s = [0] * pow_size
    binary_t = binary_s.copy()

    for i in range(size_s):
        # Include K threshold in computation of 1s
        if s_word[i] == solve_letter:
            range_ = i + k + 1
            binary_s[max(0, i - k)] += 1
            if range_ < size_s:
                binary_s[range_] -= 1

    counter = 0
    for i in range(size_s):
        counter += binary_s[i]
        binary_s[i] = int(counter > 0)

    for i in range(size_t):
        binary_t[i] = int(t_word[size_t - 1 - i] == solve_letter)

    s_array = fast_fourier_transform(binary_s, len(binary_s))
    t_array = fast_fourier_transform(binary_t, len(binary_t))

    fourier_result = []
    for idx in range(len(s_array)):
        curr_result = s_array[idx] * t_array[idx]
        fourier_result.append(curr_result)

    f_inversed = [fourier_result[0]] + list(reversed(fourier_result[1:]))
    len_inversed = len(f_inversed)
    curr_result_array = []

    for x in fast_fourier_transform(f_inversed, len_inversed):
        curr = round(x.real / len_inversed)
        curr_result_array.append(curr)

    for i in range(len(result_aggregator_array)):
        result_aggregator_array[i] += curr_result_array[i]


# Una vez que resolvemos para cada letra, contamos

final_count = 0
for i in range(size_s):
    if result_aggregator_array[i] == size_t:
        final_count += 1


sys.stdout.write(str(final_count))


"""

FFT: N log N

http://www.cs.cmu.edu/afs/andrew/scs/cs/15-463/2001/pub/www/notes/fourier/fourier.pdf

"""