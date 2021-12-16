import random
import sys

# Usage: python3 test_p2.py rand_seed

random.seed(sys.argv[1])


n = random.randint(1, 200000)
m = random.randint(1, 20)
p = max(1, random.randint(min(m, 15) - 1, min(m, 15)))
# p = 15

print(n, m, p)
for i in range(n):
    # like_count = p
    # likes = set(range(17, 21))
    like_count = random.randint(p - 1, p)
    likes = set(random.sample(range(m), like_count))
    binary_mask = "".join(["1" if i in likes else "0" for i in range(m)])
    print(binary_mask)
