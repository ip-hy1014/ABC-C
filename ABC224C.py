n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if (xy[j][0]-xy[i][0])*(xy[k][1]-xy[i][1])-(xy[k][0]-xy[i][0])*(xy[j][1]-xy[i][1]) != 0:
        ans += 1
print(ans)