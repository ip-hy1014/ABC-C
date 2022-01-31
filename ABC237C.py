# 両端の a を除いた部分文字列が回文」かつ「左端の a の個数 <= 右端の a の個数」
# つまり先頭にしか a を加えられないから左端のaの個数が右端より少なくならないとだめ。
s = input()
r = s.rstrip("a")
l = r.lstrip("a")
if l==l[::-1] and len(r)-len(l)<=len(s)-len(r):
  print("Yes")
else:
  print("No")