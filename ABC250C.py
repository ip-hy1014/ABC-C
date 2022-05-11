n,q = map(int,input().split())
a = list(range(n+1)) #i番目のボールには整数iが書かれたn個のボール
kiroku = list(range(n+1)) #xが書かれたボールがリストの何番目にあるかを記録するリスト
for _ in range(q):
  x = int(input())
  xk = kiroku[x] #xの位置
  if xk != n:
    yk = xk + 1 #右端ではない場合右隣と入れ替える
  else:
    yk = xk - 1 #右端なので左隣と入れ替える
  y = a[yk] #入れ替えるボールに書かれた数
  a[xk],a[yk] = a[yk],a[xk]
  kiroku[x] = yk #入れ替えた後の状態を記録
  kiroku[y] = xk
print(*a[1:]) #a[0]は使わないのでスライスする