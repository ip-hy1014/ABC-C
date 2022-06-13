"""
方針:場合分け
数列の中でxに一番近い数を探す
"""
x,a,d,n = map(int,input().split())
if d<0: #正規化する→等差数列の反転を行っても良い数の集合は変わらない
  x = -x
  d = -d
  a = -a
if x<=a: #xが初項以下
  print(a-x)
elif a+d*(n-1)<=x: #数列の最大値がx以下
  print(x-a-d*(n-1))
else:
  x -= a #数列Sには 0≤k≤N−1 なる全ての整数kに対して、A+kDが含まれ、さらに A≤X≤A+(N−1)D が成立するため,
  print(min(x%d,d-x%d)) #答えはmin((X−A)%D,D−(X−A)%D) → Dずつ単調増加するためXに一番近いのは2通りしかない