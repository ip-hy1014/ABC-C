n = int(input())
l = []
for i in range(n):
  l.append(input())
print(len(set(l)))

#別解
n = int(input())
s = set()
for i in range(n):
  s.add(input())
print(len(s))