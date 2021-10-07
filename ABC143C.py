n = int(input())
s = input()
ans = 1
for i in range(n-1):
  if s[i]!=s[i+1]:
    ans += 1
print(ans)

#別解
from itertools import groupby
n = int(input())
s = input()
ans = len(list(groupby(s)))
print(ans)
