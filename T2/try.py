from timeit import timeit




test = """
positional_set = set()
vector_size = 100
for ii in range(50):
    positional_set.add(ii)
    
"".join(["1" if i_ in positional_set else "0" for i_ in range(vector_size)])

"""
print(timeit(test))

test = """
positional_set = set()
vector_size = 100
for ii in range(50):
    positional_set.add(ii)

stre = ""
for i in range(vector_size):
    if i in positional_set:
        stre += "1"
    else:
        stre += "0"
"""
print(timeit(test))

