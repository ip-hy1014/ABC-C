n = int(input())
def divisor(n):
    sq = n**0.5
    border = int(sq)
    table = []
    bigs = []
    for small in range(1, border+1):
        if n%small == 0:
            table.append(small)
            big = n//small
            bigs.append(big)
    if border == sq:
        bigs.pop()
    table += reversed(bigs)
    return table
l = divisor(n)
for i in l:
  print(i)