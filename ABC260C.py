#dp
#ri: レベル i の赤い宝石を 1 個持っている状態からはじめて、入手できるレベル 1 の青い宝石の個数
#bi: レベル i の青い宝石を 1 個持っている状態からはじめて、入手できるレベル 1 の青い宝石の個数
#bn = rn−1 + bn−1 × Y
#rn = rn−1 + bn × X
n,x,y = map(int,input().split())
r = [0]*(n+1) #リストのインデックスがレベル数に対応
b = [0]*(n+1)
r[1] = 0 #新たな宝石を得ることはできない
b[1] = 1 #新たに青い宝石を得ることはできないが既に一つ持っているので1になる
for i in range(2,n+1):
  b[i]=r[i-1]+b[i-1]*y
  r[i]=r[i-1]+b[i]*x #b[i]を先に計算することに留意、なぜならr[i]を計算するのにb[i]の値が必要だから
print(r[n])