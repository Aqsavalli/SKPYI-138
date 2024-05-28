from itertools import product

s = ["I", "You"]
v = ["Play", "Love"]
o = ["Cricket", "Ludo"]

combinations = product(s, v, o)

for combination in combinations:
    print(" ".join(combination) + ".")
    