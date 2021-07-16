import collections
n = int(input())
s = [input() for _ in range(n)]
c = collections.Counter(s)
m = max(c.values())
keys = [k for k, v in c.items() if v == m]
[print(i) for i in sorted(keys)]

"""
import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(l)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})
"""

"""
for k, v in d.items():
    print(k, v)
# key1 1
# key2 2
# key3 3
"""