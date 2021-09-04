#逆置換
#順列 P=(p1​ ,p2​,…,pN​) に対して qpi​=i を満たす順列 Q=(q1​,q2,…,qN)のこと
n = int(input())
p = list(map(int,input().split()))
q = []
for i in range(n):
  q.append([p[i],i+1])
q.sort(key=lambda x: x[0])
ans = []
for i in range(n):
  ans.append(q[i][1])
print(*ans)
