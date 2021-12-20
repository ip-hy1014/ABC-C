n = int(input())
c = 0
nt,nx,ny = 0,0,0
for i in range(n):
  t,x,y = map(int,input().split())
  if abs(x-nx)+abs(y-ny)<=t-nt and t%2==(x+y)%2:
    c+=1
  nt,nx,ny = t,x,y
print('Yes' if c==n else 'No')
