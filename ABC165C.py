#重複組み合わせを列挙して数列を作り、全探索する
from itertools import combinations_with_replacement as cwr
n,m,q = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(q)]
ans = 0
for A in cwr(range(1,m+1),n): #1からmまでの数字で長さnの数列を作る
  mx = 0
  for a,b,c,d in l:
    if A[b-1] - A[a-1] == c:
      mx += d
  ans = max(ans,mx)
print(ans)