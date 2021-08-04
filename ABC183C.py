from itertools import permutations
n,k = map(int,input().split())
t = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for p in permutations(range(1,n)): #(n-1)!通り
  time = 0 #かかる時間
  toshi = 0 #スタート地点
  for i in range(n-1):
    j = p[i] #移動先
    time += t[toshi][j] #toshiからjに向かうのにかかる時間
    toshi = j
  time += t[toshi][0] #最後に都市1にもどる
  if time == k:
    ans += 1
print(ans)