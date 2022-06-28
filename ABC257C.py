#方針:体重順にソートして、最大値を子供の人数で初期化、体重が小さい方から大人に変換していき最大値となる箇所を探索する
#実数を動くって書いてあるけど実際はWi(体重)がXになる
#入力例1の場合だと、X=60とすると答えが一番大きくなる
import bisect
n = int(input())
s = input()
w = list(map(int,input().split()))
a = [] #大人
c = [] #子供
for i in range(n):
  if s[i]=="1":
    a.append(w[i])
  else:
    c.append(w[i])
a.sort() #ソートしても答えに影響はない
c.sort()
ans = len(c) #子供の人数で初期化
l = len(a)
for i in range(l):
  idx = bisect.bisect_left(c,a[i]) #大人を体重が軽い順に見ていって、どこに入るか（つまりXとなるか）探索する
  ans = max(ans,l-i+idx) #(大人の人数 - 既に子供判定された人数(e.g. X=60ならその前の体重が30の人は大人と判定されない) + 子供として判定された人数)
print(ans)