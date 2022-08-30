#itertools.combinations(iterable, r)
#入力 iterable の要素からなる長さ r の部分列を返す
#行列Aから行列Bの長さの部分列を全探索して一致するならYes,しないならNoを出力
from itertools import combinations
h1,w1 = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h1)]
h2,w2 = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(h2)]
def check(ch,cw):
  for i in range(h2):
    for j in range(w2):
      if a[ch[i]][cw[j]] != b[i][j]:
        return False
  return True
for ch in combinations(range(h1),h2):
  for cw in combinations(range(w1),w2):
    if check(ch,cw):
      print("Yes")
      exit()
print("No")