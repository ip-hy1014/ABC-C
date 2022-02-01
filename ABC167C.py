INF = 1<<60

def judge(bit):
  s = 0
  l = [0]*m
  for i in range(n):
    if not (bit & (1<<i)):
      continue
    s += c[i]
    for j in range(m):
      l[j] += a[i][j]
  for i in range(m):
    if l[i]<x:
      return INF
  return s

n,m,x = map(int,input().split())
c = [0]*n
a = [[] for _ in range(n)]
for i in range(n):
  c[i],*a[i] = map(int,input().split())
ans = INF
for bit in range(1<<n):
  ans = min(ans,judge(bit))
print(ans if ans != INF else -1)

#別解
from itertools import product
INF = 1 << 60
def calc(pro):
    S = 0
    L = [0] * M
    for i in range(N):
        if not pro[i]:
            continue
        S += C[i]
        for j in range(M):
            L[j] += A[i][j]
    for i in range(M):
        if L[i] < X:
            return INF
    return S

N, M, X = map(int, input().split())
C = [0] * N
A = [[] for _ in range(N)]
for i in range(N):
    C[i], *A[i] = map(int, input().split())
ans = INF
for pro in product((0, 1), repeat=N):
    ans = min(ans, calc(pro))
print(ans if ans != INF else -1)