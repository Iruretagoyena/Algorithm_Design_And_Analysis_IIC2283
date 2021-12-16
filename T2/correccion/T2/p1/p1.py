import cmath
import math

PI_2_J = 2j * cmath.pi
powers_of_unit = dict()

def FFT(arr):
    n = len(arr)
    if n == 2:
        a0, a1 = arr
        return [a0 + a1, a0 - a1]
    n_half = n // 2
    evens = arr[:n:2]
    odds = arr[1:n:2]
    y_0 = FFT(evens)
    y_1 = FFT(odds)
    y = [0] * n
    for k in range(n_half):
        alpha = powers_of_unit[n][k]
        a = y_0[k]
        b = alpha * y_1[k]
        y[k] = a + b
        y[n_half + k] = a - b
    return y

def mult(arr_1, arr_2):
    f_1 = FFT(arr_1)
    f_2 = FFT(arr_2)
    m = len(f_1)
    f_result = [a*b for a, b in zip(f_1, f_2)]
    f_inversed = [f_result[0]] + list(reversed(f_result[1:]))
    m = len(f_inversed)
    result = [round(x.real / m) for x in FFT(f_inversed)]
    return result

def precompute_powers(n):
    n_value = n
    while n_value >= 4:
        powers_of_n = dict()
        for k_value in range(0, n_value // 2):
            power = cmath.exp(PI_2_J * k_value / n_value)
            powers_of_n[k_value] = power
        powers_of_unit[n_value] = powers_of_n
        n_value = n_value // 2

if __name__ == "__main__":
    n_s, n_t, k = map(int, input().split())
    s = input()
    t = input()
    t = t[::-1]
    n_with_padding = 2**math.ceil(math.log2(n_s + n_t))
    precompute_powers(n_with_padding)
    counts = [0] * n_with_padding

    for c in "ACGT":
        ones_s = [0] * n_with_padding
        for i in range(n_s):
            if s[i] == c:
                a = max(0, i - k)
                b = i + k + 1
                ones_s[a] += 1
                if b < n_s: ones_s[b] -= 1
        tmp = 0
        for i in range(n_s):
            tmp += ones_s[i]
            ones_s[i] = int(tmp > 0)
        ones_t = [0] * n_with_padding
        for i in range(n_t): ones_t[i] = int(t[i] == c)
        result = mult(ones_s, ones_t)        
        for i in range(len(counts)): counts[i] += result[i]

    ans = sum(1 for i in range(n_s) if counts[i] == n_t)
    print(ans)