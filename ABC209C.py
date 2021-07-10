n = int(input())
c = list(map(int, input().split()))
c.sort()
ans = 1
for i in range(n):
  ans = ans * max(0,c[i]-i) % 1000000007
print(ans)

# https://qiita.com/Euglenese/items/2c9975d174dd5bd28d64