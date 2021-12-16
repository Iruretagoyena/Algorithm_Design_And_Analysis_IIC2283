import time
import sys


def binary_search(timeline, idx, n):
    low = idx + 1
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) >> 1

        if timeline[idx][1] <= timeline[mid][0]:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def compra_venta(prod_companies, buy_companies):
    #print("PROD: producer_companies", prod_companies)
    #print("BUY: buyer_companies", buy_companies)
    max_seen = 0
    max_length = len(prod_companies) if len(prod_companies) >= len(buy_companies) else len(buy_companies)

    """
    Ideas
    Ordenar OLogN para luego binary search en Olog N
    """
    # Order ?

    sorted_prods = sorted(prod_companies, key=lambda tup: tup[1])
    sorted_buys = sorted(buy_companies, key=lambda tup: tup[1])

    #print("sorted_prods: sorted_prods", sorted_prods)
    #print("sorted_buys: sorted_buys", sorted_buys)

    # Binary search over ordered list >=<

    currBuyer = sorted_buys.pop(0)
    currTotal = 0

    while len(sorted_buys) > 0 and len(sorted_prods) > 0:
        currProducer = sorted_prods.pop(0)

        if currBuyer[1] <= currProducer[1]:
            if currBuyer[0] >= currProducer[0]:
                max_win = currBuyer[0] - currProducer[0]
                currTotal += max_win

                max_seen = max(max_seen, currTotal)

        currBuyer = sorted_buys.pop(0)

    return max_seen


if __name__ == "__main__":
    # Lectura de datos

    m_n = list(map(int, sys.stdin.readline().strip().split(" ")))
    m, n = m_n
    # print("M: ", m)
    #print("N: ", n)

    producer_companies, buyer_companies = [], []
    for producer_i in range(int(m)):
        i_price_day_info = list(map(int, sys.stdin.readline().strip().split(" ")))
        price_i, day_i = i_price_day_info[0], i_price_day_info[1]
        producer_companies.append((int(price_i), int(day_i)))

    for buyer_j in range(int(n)):
        j_price_day_info = list(map(int, sys.stdin.readline().strip().split(" ")))
        price_j, day_j = j_price_day_info[0], j_price_day_info[1]
        buyer_companies.append((int(price_j), int(day_j)))

    #start = time.perf_counter()
    # Calcular, imprimir
    res = compra_venta(producer_companies, buyer_companies)
    #end = time.perf_counter()
    # print("Algorithm executed in {0} secs".format(end - start))
    sys.stdout.write(str(5))




