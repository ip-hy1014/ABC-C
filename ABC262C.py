#ai=i かつ aj=j → n(n-1)/2個
#ai=j かつ aj=i
#上記それぞれの個数を求める

n = int(input())
a = [0]+list(map(int,input().split()))
c = 0
for i in range(1,n+1):
  if a[i]==i:
    c+=1
ans = c*(c-1)//2
for i in range(1,n+1):
  j=a[i]
  if i<j and a[j]==i:
    ans+=1
print(ans)
