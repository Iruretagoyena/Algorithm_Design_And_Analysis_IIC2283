from collections import Counter
import sys
import random


def ncr(n_, r):
    r = min(r, n_-r)
    numer = reduce(op.mul, range(n_, n_-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom



def set_to_sparse_vector(positional_set, vector_size):
    return "".join(["1" if i_ in positional_set else "0" for i_ in range(vector_size)])


def to_positional_set(array):
    _set = set()
    for idx_, char_, in enumerate(array):
        if char_ == "1":
            _set.add(idx_)
    return _set


def random_bit_combination(positional_set, sample_size):
    if sample_size >= len(positional_set):
        return positional_set

    if sample_size == 0:
        return set()

    new_set = set()

    for iteration in range(sample_size + 1):
        # print("sample_size", sample_size, positional_set)
        el = random.sample(positional_set, 1)[0]
        positional_set.remove(el)
        new_set.add(el)

    return new_set


def monte_carlo_positional_set(total_rows, total_cols, interests, max_interest_amount):
    min_interest = (total_rows + 1) // 2

    # sum() by columns - N*M complexity
    count_ones = [0] * total_cols
    for idx_ in range(total_cols):
        for pos_set in interests:
            if idx_ in pos_set:
                count_ones[idx_] += 1

    # filter the ones at least ceil(n/2)
    bit_meets_condition = set()
    for col in range(total_cols):
        if count_ones[col] >= min_interest:
            bit_meets_condition.add(col)

    # early exit, return empty set
    total_possible_bits = len(bit_meets_condition)
    if total_possible_bits == 0:
        return bit_meets_condition

    # print("bit_meets_condition", bit_meets_condition, total_possible_bits)

    # generate random combinations, check if they are at least ceil(n/2) times in matrix
    best_option_seen = []
    len_best_seen = 0

    # for jj in range(100):
    for try_answer_size in range(total_possible_bits + 1):

        # N chooses K
        tries = ncr(total_possible_bits, try_answer_size)
        # print("tries", tries)

        for try_ in range(tries + 1):
            try_bit_combination = random_bit_combination(bit_meets_condition, try_answer_size)
            # print("try_bit_combination", try_bit_combination)

            # Check each row in matrix for this newly generated vector. appears >= ceil(n/2)a
            seen = 0
            for row in range(total_rows):
                curr_interest_row = interests[row]

                # Check is all random interests are in curr_row
                if len(try_bit_combination.difference(curr_interest_row)) == 0:
                    seen += 1

                if seen >= min_interest:  # I've seen it enough times.
                    candidate_len = len(try_bit_combination)
                    if candidate_len > len_best_seen:  # Is it the best answer so far ?
                        best_option_seen = try_bit_combination.copy()
                        # print("BEST", best_option_seen)
                        len_best_seen = candidate_len
                        break  # Break regardless of outcome

    return best_option_seen


def monte_carlo_binary_representation(total_rows, total_cols, interests, max_interest_amount):
    longest_so_far = (0, 0)
    for iteration in range(40):
        current_random_choice = random.choice(interests)
        curr_choice = current_random_choice
        # Crear counter de binario transormado a int
        cripto_counter = dict(Counter((person & current_random_choice for person in interests)))
        # print(cripto_counter)
        seen_criptos = {}

        while curr_choice > 0:
            seen_criptos[curr_choice] = 0
            curr_choice = (curr_choice - 1) & current_random_choice

        cols = total_cols
        max_p = max_interest_amount
        min_interest = (total_rows + 1) // 2

        for counter_key in cripto_counter.keys():
            curr_choice = counter_key

            while curr_choice > 0:
                seen_criptos[curr_choice] += cripto_counter[counter_key]
                curr_choice = (curr_choice - 1) & counter_key

        # Para lo que vimos, ver si alguno cumple la regla del interes minimo
        for curr_choice, idx in seen_criptos.items():
            if min_interest <= idx:
                count_ones = (bin(curr_choice).count("1"), curr_choice)
                longest_so_far = max(count_ones, longest_so_far)

        return longest_so_far


n, m, p = list(map(int, sys.stdin.readline().strip().split(" ")))
amigos = []
for i in range(n):
    read_line = int(sys.stdin.readline().strip(), 2)
    amigos.append(read_line)

result = monte_carlo_binary_representation(n, m, amigos, p)
#  result_string = ""
print("{{:0{}b}}".format(m).format(result[1]))
