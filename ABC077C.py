#二分探索
#jを固定してi,kの積を求める
#bより小さいa,bより大きいcはいくつあるか
import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
ans = 0
for bb in b:
  aa = bisect.bisect_left(a,bb)
  cc = bisect.bisect_right(c,bb)
  ans += aa*(len(c)-cc)
print(ans)

#別解
import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
ans = 0
for j in range(n):
  i = bisect.bisect_left(a,b[j])
  k = bisect.bisect_right(c,b[j])
  ans += i*((n-1)-k+1)
print(ans)