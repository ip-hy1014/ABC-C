n = int(input())
ans = 10**18
for i in range(1,int(n**0.5)+1): #対称性からi<=jとしてよく、i<=sqrt(n)で全探索
  if n%i==0:
    ans = min(ans,n//i+i-2) #j := n/i
print(ans)