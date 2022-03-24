n = int(input())
sq = int(n**0.5)
s = set()
for i in range(2,sq+1):
  a = i*i
  while a<=n:
    s.add(a)
    a*=i
print(n-len(s))