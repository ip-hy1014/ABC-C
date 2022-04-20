x,y = map(int,input().split())
ans = 1
i = x
while i*2<=y:
  i*=2
  ans+=1
print(ans)