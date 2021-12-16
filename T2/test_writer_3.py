from random import randint, shuffle
from math import ceil

if __name__ == "__main__":
  with open("test.txt", 'w', encoding='utf-8') as file:
    n = randint(10**3, 2*10**5)
    m = randint(10**0, 60)
    p = randint(1, m)
    if p > 15:
      p = randint(1, 15)
    file.write(str(n) + " " + str(m) + " " + str(p) + "\n")

    r = randint(1, p)
    resp = ["1"] * r + ["0"] * (m - r)
    shuffle(resp)
    resp = "".join(resp)
    print(resp)
    people = []
    max_p = randint(ceil(n/2), n)
    for i in range(max_p):
      person = ""
      for coin in resp:
        if coin == "1": person += "1"
        else: person += "1" if randint(1, 10) == 1 else "0"
      people.append(person)
    for i in range(max_p, n):
      k = randint(0, p)
      person = ["1"] * k + ["0"] * (m - k) 
      shuffle(person)
      people.append("".join(person))
    shuffle(people)
    for person in people:
      file.write(person + "\n")