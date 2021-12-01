"""
今まで出てきた数字の中で、P[i]が最小値となる回数が答え
つまり、順列が降順にソートされていたら、ans==Nとなる
"""
n = int(input())
p = list(map(int,input().split()))
mn = 10**18
ans = 0
for i in range(n):
  mn = min(mn,p[i])
  if mn==p[i]:
    ans += 1
print(ans)