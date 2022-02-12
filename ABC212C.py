from bisect import bisect_left
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 10**10
a.sort()
for i in b:
  j = bisect_left(a,i)
  if j>0: #配列外参照を起こさないように
    ans = min(ans,abs(a[j-1]-i))
  if j<n:
    ans = min(ans,abs(a[j]-i))
print(ans)