#２進数に変換する
n = int(input())
ans = bin(n)[2:]
print(ans.replace("1","BA").replace("0","B"))