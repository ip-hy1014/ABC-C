"""
Xにおいて何番目に登場するか表す数値に置き換えてからソート
sort(key=lambda x: 【keyにしたい要素】)
"""
s = input()
n = int(input())
l = []
for _ in range(n):
  l.append(input())
l.sort(key=lambda x: [s.index(i) for i in x]) #与えられた新たなアルファベット順をKeyにしてソート
for ans in l:
  print(ans)