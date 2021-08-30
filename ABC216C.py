#２進数に変換する
n = int(input())
ans = bin(n)[2:]
print(ans.replace("1","BA").replace("0","B"))

#別解
#nが0になるまでループさせる
n = int(input())
ans = ""
while n > 0:
  if n % 2 == 0:
    n = n // 2
    ans = "B" + ans
  else:
    n -= 1
    ans = "A" + ans
print(ans)
