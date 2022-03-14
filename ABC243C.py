"""
rmin : キーを k としたとき、y=k でありかつ右を向いている人のうち最も x 座標が小さい人
lmax : キーを k としたとき、y=k でありかつ左を向いている人のうち最も x 座標が大きい人
"""

from collections import defaultdict
INF = 10**18
n = int(input())
xy = [list(map(int,input().split())) for  _ in range(n)]
S = input()
lmax = defaultdict(lambda: -INF)
rmin = defaultdict(lambda: INF)
ans = "No"
for s,(x,y) in zip(S,xy):
  if s=="L":
    lmax[y] = max(lmax[y],x) #左を向いていて最もx座標が大きい人
  else:
    rmin[y] = min(rmin[y],x) #右を向いていて最もx座標が小さい人
for y in lmax.keys():
  if rmin[y]<lmax[y]:
    ans = "Yes"
print(ans)