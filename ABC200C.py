n = int(input())
a = list(map(int,input().split()))
ans = 0
a_l = [0]*200
for i in range(n):
  A = a[i]%200
  a_l[A] += 1
for i in a_l:
  ans += i*(i-1)//2
print(ans)