#正直か否かの2通りしかない、そしてNが高々15なのでbit全探索する
#正直者とされる人の証言だけチェックする
n = int(input())
xy = [[] for _ in range(n)] #証言のデータを格納、人iが「人xはyである」と証言しているときxy[i][x]=yである
for i in range(n):
  a = int(input())
  for _ in range(a):
    x,y = map(int,input().split())
    xy[i].append((x-1,y)) #0-indexedでx-1で格納
ans = 0
for i in range(1<<n): #2**nと同じ
  ok = True
  c = 0
  for j in range(n):
    if (i>>j & 1) == 0: #正直者の証言(1)だけ確認するので、不親切な人(0)はスルー
      continue
    c += 1
    for x,y in xy[j]:
      if (i>>x & 1) != y:
        ok = False
  if ok:
    ans = max(ans,c)
print(ans)

#別解
from itertools import *
n = int(input())
g = []
for i in range(n):
  a = int(input())
  for _ in range(a):
    x,y = map(int,input().split())
    g.append((i,x-1,y)) #証言のデータを格納、人iが「人xはyである」と証言しているときg[i][x]=yである
ans = 0
for i in product([0,1],repeat=n):
  ok = True
  for j in g:
    if i[j[0]]==1 and i[j[1]]!=j[2]: #正直者の証言だけ確認し、その証言に矛盾があった場合False
      ok = False
      break
  if ok:
    ans = sum(i)
print(ans)

"""
入力例1の場合の証言データ
[(0, 1, 1), (1, 0, 1), (2, 1, 0)]

n = 3の場合の正直者か否かの全パターン
(1, 1, 1)
(1, 1, 0)
(1, 0, 1)
(1, 0, 0)
(0, 1, 1)
(0, 1, 0)
(0, 0, 1)
(0, 0, 0)

i[j[0]]==1の部分は、上の全パターンを一つずつ見ていく
"""

"""
i[j[0]],i[j[1]],j[2]を順に出力
0 0 1
0 0 1
0 0 0
0 0 1
0 0 1
1 0 0
0 1 1
1 0 1
0 1 0
0 1 1
1 0 1
1 1 0
1 0 1
0 1 1
0 0 0
1 0 1
0 1 1
1 0 0
1 1 1
1 1 1
0 1 0
1 1 1
1 1 1
1 1 0
"""
