x,n = map(int,input().split())
p = list(map(int,input().split()))
for i in range(101):
  if x-i not in p:
    print(x-i)
    exit()
  if x+i not in p:
    print(x+i)
    exit()