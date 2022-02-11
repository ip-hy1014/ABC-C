n = int(input())
for i in range(1,10**7):
  s = str(i)*2
  x = int(s)
  if x>n:
    print(i-1)
    exit()