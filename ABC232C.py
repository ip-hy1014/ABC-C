# 同形写像
# 番号を振り直して一致させることができるかどうか判定する
import itertools
n,m = map(int,input().split())
a = [[False]*n for _ in range(n)]
b = [[False]*n for _ in range(n)]
for _ in range(m):
  c,d = map(int,input().split())
  c -= 1
  d -= 1
  a[c][d] = a[d][c] = True
for _ in range(m):
  c,d = map(int,input().split())
  c -= 1
  d -= 1
  b[c][d] = b[d][c] = True
ans = False
for p in itertools.permutations(range(n)):
  ok = True
  for i in range(n):
    for j in range(n):
      if a[i][j] != b[p[i]][p[j]]:
        ok = False
  if ok:
    ans = True
print("Yes" if ans else "No")
