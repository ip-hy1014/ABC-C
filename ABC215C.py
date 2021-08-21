import itertools
s,k = input().split()
k = int(k)
l = []
for all in itertools.permutations(s):
  l.append("".join(all))
ans = list(set(l))
ans.sort()
print(ans[k-1])