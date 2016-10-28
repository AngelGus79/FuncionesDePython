from collections import Counter
l = [1, 1, 2, 2, 3, 4, 5, 6]
c = Counter(l)

for x, y in c.items():
    print(x, y)
