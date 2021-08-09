from operator import mul
from functools import reduce
l = int(input())
def combinations_count(n,r):
  r = min(r,n-r)
  numer = reduce(mul, range(n, n-r, -1), 1)
  denom = reduce(mul, range(1, r+1), 1)
  return numer // denom
print(combinations_count(l-1, 12))

#別解
from math import comb
l = int(input())
ans = comb(l-1, 11)
print(ans)