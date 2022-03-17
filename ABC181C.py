n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      x,y = xy[i]
      x1,y1 = xy[j]
      x2,y2 = xy[k]
      if (x2-x1)*(y-y1)==(x-x1)*(y2-y1):
        print("Yes")
        exit()
print("No")