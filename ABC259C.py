"""
ある文字が2つ以上続いているなら文字数を増やすことが可能
1文字しかない場合は増やすことができず、また減らすこともできない

「No」となるのは以下の4パターン
・文字の種類数が違う
・文字の種類が違う
・Sが1文字
・T側よりS側の文字が多い
"""

def rlg(s):
  now = s[0] #いま連続している文字
  c = 1 #連続している文字数
  l = [] #何文字連続しているか記録
  for i in range(1,len(s)):
    if now != s[i]: #sのi文字目がnowじゃないなら
      l.append([now,c]) #リストに記録
      now = s[i] #次の文字へ
      c = 1
    else: #sのi文字目がnowならインクリメント
      c += 1
  l.append([now,c]) #最後のカウントを追加
  return l

S = input()
T = input()
s = rlg(S)
t = rlg(T)

if len(s) != len(t): #文字の種類数が違う場合
  print("No")
  exit()

for i in range(len(t)):
  if s[i] != t[i]:
    if s[i][0] != t[i][0] or s[i][1] > t[i][1] or s[i][1]==1: #文字の種類が違う or T側よりS側の文字が多い or Sが1文字
      print("No")
      exit()
print("Yes")