def main():
  def get(x):
    if x<n:
      return 0,x
    else:
      return 1,x-n
  n = int(input())
  s = input()
  q = int(input())
  c = list(s[:n])
  d = list(s[n:])
  l = [c,d]
  for i in range(q):
    t,a,b = map(int,input().split())
    a -= 1
    b -= 1
    if t == 1:
      ai,aj = get(a)
      bi,bj = get(b)
      l[ai][aj],l[bi][bj] = l[bi][bj],l[ai][aj]
    else:
      l[0],l[1] = l[1],l[0]
  s = l[0]+l[1]
  print("".join(s))
if __name__ == '__main__':
    main()