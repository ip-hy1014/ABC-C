#累積和
n,m = map(int,input().split())
a = [0]+list(map(int,input().split()))
ans = 0

#初項部分は愚直に計算しておく
for i in range(1,m+1):
  ans += i*a[i]

#累積和の計算
c = [0]*(n+1)
for i in range(1,n+1):
  c[i] = c[i-1]+a[i]

# mx：「B1=Ai(B：Ai A(i+1) A(i+2) ... A(i+M-1)の場合」のΣi*Biの値
mx = ans
for i in range(2,n-m+2):
      # 「B1=Ai(B：Ai A(i+1) A(i+2) ... A(i+M-1))の場合」=「B1=A(i-1)(B：A(i-1) Ai A(i+1) ... A(i+M-2))の場合」-(「A(i-1)~A(i+M-2)の和」)+A(i+M-1)*M
  mx = mx-(c[i+m-2]-c[i-2]) + a[i+m-1]*m
  ans = max(ans,mx)
print(ans)

#別解
n,m = map(int,input().split())
A = list(map(int,input().split()))

sigma=sum([(i+1)*a for i,a in enumerate(A[:m])]) #最初だけO(M)で計算
sumB = sum(A[:m]) #累積和
result =sigma

for i in range(n-m):
  sigma = sigma - sumB+ m*A[i+m]
  sumB = sumB - A[i] + A[i+m] #最もインデックスの小さい項を引き、次の項を足して更新
  if sigma>result:
    result = sigma
print(result)