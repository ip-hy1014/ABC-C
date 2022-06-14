#制約がN<=20なのでbit全探索を用いる
from itertools import product
n = int(input())
a = list(map(int,input().split()))
ans = 1<<60 #最小値を求めるので必要十分に大きい数で初期化
for b in product((True,False),repeat=n-1): #bit全探索をするのにproductを使用する
  bit = list(b)+[True] #bit[i]がTrueであればa[i]とa[i+1]の間に区切り棒があり、a[n-1]の右に常に区切り棒があることにする(配列外参照を防ぐため)
  x = 0 #各区間のXOR
  o = 0 #各区間のOR
  for i in range(n):
    o |= a[i] #各区間でORを計算
    if bit[i]: #区切り棒(True)がきたらXORを計算する
      x ^= o
      o = 0 #次の区間の計算のために0にする
  ans = min(ans,x)
print(ans)