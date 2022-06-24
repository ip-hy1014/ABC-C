# 方針:累積和からの二分探索
# Aを上から何冊読むかを決めるとBに使える残り時間は、K-(Aの本を読むのに使った時間の合計)分となる
# ∴ Aを決めればBを上から何冊読めるかが自動的に決まる

from itertools import accumulate
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
aa = [0]+list(accumulate(a)) #aを1冊も読まない場合があるので[0]を追加する
bb = [0]+list(accumulate(b))
ans = 0
for i in range(n+1):
  c = k-aa[i] #c = K-(Aの本を読むのに使った時間の合計)分
  if c<0: #k分を超えたらbreak
    break
  ok = 0
  ng = m+1 #最初は 0 <= x < m+1 の範囲で、この範囲を狭めていく
  while abs(ng-ok)>1: #ng = ok + 1のとき、ok <= x < ng は ok <= x < ok + 1で、x = okに確定
    mid = (ok+ng)//2
    if bb[mid]<=c: #bをmid冊読めるか
      ok = mid #読めるなok
    else:
      ng = mid #読めないならng
  j = ok
  ans = max(ans,i+j)
print(ans)