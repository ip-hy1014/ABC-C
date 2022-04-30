n,k = map(int,input().split())
s = [input() for _ in range(n)]
ans = 0
for i in range(1<<n):
  c = [0]*26
  for j in range(n):
    if i>>j & 1:
      for l in s[j]:
        c[ord(l)-ord("a")] += 1
  d = 0
  for j in range(26):
    if c[j] == k:
      d += 1
  ans = max(ans,d)
print(ans)