"""
max()関数を使うと計算量がO(N^2)になる
今までで一番背の高い人を保持して，一人見るたびに更新する.
"""
n = int(input())
a = list(map(int,input().split()))
ans = 0
cm = 0 #そのとき一番背の高い人
for i in a:
  if cm > i:
    ans += cm - i
  cm = max(cm,i)
print(ans)

#別解
n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(1,n):
  if a[i-1]>a[i]:
    ans += a[i-1]-a[i]
    a[i] = a[i-1]
print(ans)