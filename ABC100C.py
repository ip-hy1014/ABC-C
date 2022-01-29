# 全部奇数になったら終わり
# それぞれの要素が2で割れる回数の合計が答え
n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
  while i%2==0:
    i //= 2
    ans += 1
print(ans)