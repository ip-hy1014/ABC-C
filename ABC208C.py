n,k = map(int, input().split())
q = k//n
r = k%n
a = list(map(int, input().split()))
a_x = sorted(a)[r]
for i in a:
  if i < a_x:
    print(q+1)
  else:
    print(q)