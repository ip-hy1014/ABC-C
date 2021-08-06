from itertools import permutations
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
l = []
for i in permutations(range(1,n+1)):
  l.append(list(i))
ans = abs((l.index(p)+1) - (l.index(q)+1))
print(ans)