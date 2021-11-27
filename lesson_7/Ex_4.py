import os

sizes = []
for root, dirs, files in os.walk('.\\'):
    if files:
        for f in files:
            sizes.append(os.path.getsize(os.path.join(root, f)))

result = {}
for i in range(1, len(str(max(sizes))) + 1):
    result.setdefault(10**i, 0)
for s in sizes:
    x = 10 ** (len(str(s)))
    result[x] += 1
print(result)
