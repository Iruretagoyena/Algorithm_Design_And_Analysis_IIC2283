def fft(arr, inv):
    n = len(arr)

    rev = [0] * n
    for i in range(n):
        rev[i] = rev[i >> 1] >> 1
        if i & 1:
            rev[i] |= n >> 1
        if i < rev[i]:
            arr[i], arr[rev[i]] = arr[rev[i]], arr[i]

    mod = 7340033
    root = pow(5, mod - 2, mod) if inv else 5
    root_pw = 1 << 20

    l = 2
    lg = 1
    while l <= n:
        wn = pow(root, root_pw >> lg, mod)
        for i in range(0, n, l):
            w = 1
            for j in range(l >> 1):
                u = arr[i + j]
                v = (w * arr[i + j + (l >> 1)]) % mod
                arr[i + j] = (u + v) if (u + v < mod) else (u + v - mod)
                arr[i + j + (l >> 1)] = (u - v + mod) if (u - v < 0) else (u - v)
                w = (w * wn) % mod
        l <<= 1
        lg += 1

    if inv:
        mult = pow(n, mod - 2, mod)
        for i in range(n):
            arr[i] = (arr[i] * mult) % mod


def main():
    import sys
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    s = input()[:-1]
    t = input()[:-1]
    N = 2 << (n - 1).bit_length()

    sA = [0] * N
    sT = [0] * N
    sG = [0] * N
    sC = [0] * N
    tA = [0] * N
    tT = [0] * N
    tG = [0] * N
    tC = [0] * N

    for i in range(n):

        if s[i] == 'A':
            sA[N - n + i] = 1
            j = 1
            while j <= k and j <= i and not sA[N - n + i - j]:
                sA[N - n + i - j] = 1
                j += 1
            j = 1
            while j <= k and j < n - i:
                sA[N - n + i + j] = 1
                j += 1

        elif s[i] == 'T':
            sT[N - n + i] = 1
            j = 1
            while j <= k and j <= i and not sT[N - n + i - j]:
                sT[N - n + i - j] = 1
                j += 1
            j = 1
            while j <= k and j < n - i:
                sT[N - n + i + j] = 1
                j += 1

        elif s[i] == 'G':
            sG[N - n + i] = 1
            j = 1
            while j <= k and j <= i and not sG[N - n + i - j]:
                sG[N - n + i - j] = 1
                j += 1
            j = 1
            while j <= k and j < n - i:
                sG[N - n + i + j] = 1
                j += 1

        else:
            sC[N - n + i] = 1
            j = 1
            while j <= k and j <= i and not sC[N - n + i - j]:
                sC[N - n + i - j] = 1
                j += 1
            j = 1
            while j <= k and j < n - i:
                sC[N - n + i + j] = 1
                j += 1

    for i in range(m):
        if t[~i] == 'A':
            tA[N - m + i] = 1
        elif t[~i] == 'T':
            tT[N - m + i] = 1
        elif t[~i] == 'G':
            tG[N - m + i] = 1
        else:
            tC[N - m + i] = 1

    fft(sA, 0)
    fft(sT, 0)
    fft(sG, 0)
    fft(sC, 0)
    fft(tA, 0)
    fft(tT, 0)
    fft(tG, 0)
    fft(tC, 0)

    mod = 7340033

    for i in range(N):
        sA[i] = (sA[i] * tA[i]) % mod
        sT[i] = (sT[i] * tT[i]) % mod
        sG[i] = (sG[i] * tG[i]) % mod
        sC[i] = (sC[i] * tC[i]) % mod

    fft(sA, 1)
    fft(sT, 1)
    fft(sG, 1)
    fft(sC, 1)

    ans = 0
    for i in range(N - 1 - n, N - m):
        if sA[i] + sT[i] + sG[i] + sC[i] == m:
            ans += 1
    print(ans)

    return 0


main()