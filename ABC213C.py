#座標圧縮
from bisect import bisect_left
h,w,n = map(int,input().split())
l = []
a_s = set()
b_s = set()
for i in range(n):
  a,b = list(map(int,input().split()))
  l.append([a,b])
  a_s.add(a)
  b_s.add(b)
a_l = sorted(list(a_s))
b_l = sorted(list(b_s))
for i in range(n):
  ans_a = bisect_left(a_l,l[i][0])
  ans_b = bisect_left(b_l,l[i][1])
  print(ans_a+1,ans_b+1)