from itertools import combinations
n = int(input())
l = [input()[0] for _ in range(n)]
ans = sum(a * b * c for a,b,c in combinations([l.count(s) for s in "MARCH"], 3))
print(ans)


#別解
from collections import Counter
from itertools import combinations
n = int(input())
s = [input()[0] for _ in range(n)]
s_c = Counter(s) # Counter({'H': 2, 'M': 1, 'R': 1, 'O': 1})
l = []
for c in 'MARCH':
    if c in s_c:
        l.append(s_c[c])
ans = 0
for a, b, c in combinations(l, 3):
    ans += a * b * c
print(ans)