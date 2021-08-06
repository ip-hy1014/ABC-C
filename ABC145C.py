import math
n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for x1,y1 in xy:
  for x2,y2 in xy:
    ans += math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(ans/n)

#別解
n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
  for j in range(n):
    ans += ((xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2)**0.5
print(ans/n)
