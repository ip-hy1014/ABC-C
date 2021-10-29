n = int(input())
a = list(map(int,input().split()))
h = 2**n//2
block1 = max(a[:h])
block2 = max(a[h:])
ans = min(block1,block2)
print(a.index(ans)+1)

"""
方針：選手の中で一番レートが高い人が優勝する → 優勝選手がいるブロックの逆側のブロックで一番レートが高い人が準優勝者で答え
1. ブロックを2つに分ける
2. それぞれのブロックで一番レートが高い人が決勝に進む
3. レートが低い方の選手の番号が求める答え
"""