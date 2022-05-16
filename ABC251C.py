n = int(input())
s,t = [],[]
for _ in range(n):
  a,b = input().split()
  s.append(a)
  t.append(int(b))
ans = -1
mx = -1
se = set() #登場した文字列を管理する
for i in range(n):
  if s[i] in se:
    continue #既存文字列の場合は何もしない
  se.add(s[i])
  if mx < t[i]: #オリジナル文字列の場合は得点t[i]と今までの最高得点を比較する
    ans = i
    mx = t[i]
print(ans+1)