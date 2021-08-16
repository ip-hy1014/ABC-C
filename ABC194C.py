#x が cx 個、y が cy 個あるとする
#このとき、x と y の組は cx×cy 組ある
# 1 組につき (x−y)^2 だけ答えが増えるので、cx×cy×(x−y)^2 を足せばいい
from collections import Counter
n = int(input())
a = list(map(int,input().split()))
ans = 0
c = Counter(a)
for i in range(-200,201):
  for j in range(i+1,201):
    ci = c[i]
    cj = c[j]
    ans += ci*cj*(i-j)**2
print(ans)