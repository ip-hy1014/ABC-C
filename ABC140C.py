"""
特定のAiのとり得る最大値は、Bの隣り合う要素の最小値と同じになる
最初と最後だけこの条件から異なる値となるので最後に合わせる
b[0]+b[n-2]+sum(b[i]~b[i-1])
"""

n = int(input())
b = list(map(int,input().split()))
ans = 0
for i in range(1,n-1):
  ans += min(b[i],b[i-1])
print(ans+b[0]+b[n-2])