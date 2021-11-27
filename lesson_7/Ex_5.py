import json
import os

stat_files = []
for root, dirs, files in os.walk('.\\'):
    if files:
        for f in files:
            size = os.path.getsize(os.path.join(root, f))
            ext = os.path.splitext(f)[1][1:]
            stat_files.append((size, ext))

r_sizes = {}
r_ext = {}
max_size = max(stat_files, key=lambda x: x[0])
for i in range(1, len(str(max_size[0])) + 1):
    r_sizes.setdefault(10 ** i, 0)
    r_ext.setdefault(10 ** i, [])

for s in stat_files:
    x = 10 ** (len(str(s[0])))
    r_sizes[x] += 1
    if s[1] and s[1] not in r_ext[x]:
        r_ext[x].append(s[1])

result = {k: (r_sizes[k], r_ext[k]) for k in r_sizes.keys()}

with open(f'{os.path.basename(os.path.abspath(os.curdir))}_summary.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(result))
