import sys
import sympy


ITERATIONS = 100
MIN = int(sys.argv[1].strip())
MAX = int(sys.argv[2].strip())
NUMBER = int(sys.argv[3].strip())


if __name__ == "__main__":
    if NUMBER == -1:
        print("-1")
    elif NUMBER <= MIN or NUMBER >= MAX:
        print("0")
    elif NUMBER == 1:
        print("0")
    else:
        for _ in range(ITERATIONS):
            if not sympy.isprime(NUMBER):
                print("0")
                sys.exit()
        print("1")
