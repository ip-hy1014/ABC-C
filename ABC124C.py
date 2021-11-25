"""
パターンとしては、白黒白黒… or 黒白黒白… しかない。
この2つのパターンと何箇所異なっているか調べて、小さい方を出力。
"""

s = list(input())
ans = 0
for i in range(1,len(s)):
  if s[i-1]==s[i]=="0":
    ans += 1
    s[i]="1"
  if s[i-1]==s[i]=="1":
    ans += 1
    s[i]="0"
print(ans)

#別解
s = input()
a = s[::2].count("0")+s[1::2].count("1")
b = s[::2].count("1")+s[1::2].count("0")
print(min(a,b))