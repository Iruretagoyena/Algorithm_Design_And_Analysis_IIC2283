from collections import defaultdict
from typing import List


FILENAME = "tests/primes.txt"


def sieve(sieved: defaultdict, bottom: int, top: int) -> defaultdict:
    for sieving in range(bottom + 1, top + 1):
        if not sieved[sieving]:
            multiple = sieving * sieving

            while multiple <= top:
                sieved[multiple] = True
                multiple += sieving
    return sieved


def interpret_sieved(sieved: defaultdict) -> List[int]:
    return [index for index, value in sieved.items() if not value][2:]


def write_to_file(filename: str, content: str) -> None:
    with open(filename, "w") as raw_file:
        raw_file.write(content)


if __name__ == "__main__":
    PREVIOUS_VALUE = 1
    CURRENT_VALUE = 10 ** 100
    INCREMENT = 2
    sieved = defaultdict(lambda: False)
    try:
        while True:
            print(f"Sieving to {CURRENT_VALUE}...")
            sieved = sieve(sieved, PREVIOUS_VALUE, CURRENT_VALUE)
            PREVIOUS_VALUE = CURRENT_VALUE
            CURRENT_VALUE *= INCREMENT
    except KeyboardInterrupt:
        print(f"\nWriting primes into {FILENAME}...")
        primes = interpret_sieved(sieved)
        write_to_file(FILENAME, str(primes))
