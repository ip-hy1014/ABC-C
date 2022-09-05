#四角形の3点で三角形を作った場合、4つ目の点が三角形の外側にあればYes、内側にあればNoとなる
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))

def vec(a,b):
    return (a[0]-b[0],a[1]-b[1])

def InTrianble(a,b,c,p): #三角形abcの内部に点pがあるなら内部ならFalseを返す
    ab=vec(b,a)
    bp=vec(p,b)
    bc=vec(c,b)
    cp=vec(p,c)
    ca=vec(a,c)
    ap=vec(p,a)
    OP1=ab[0]*bp[1]-ab[1]*bp[0]
    OP2=bc[0]*cp[1]-bc[1]*cp[0]
    OP3=ca[0]*ap[1]-ca[1]*ap[0]
    if (OP1>0 and OP2>0 and OP3>0) or (OP1<0 and OP2<0 and OP3<0):
        return False

# 三角形ABCの内側にDがあるか？
# 三角形BCDの内側にAがあるか？
# 三角形CDAの内側にBがあるか？
# 三角形DABの内側にCがあるか？
if InTrianble(a,b,c,d)==False or InTrianble(b,c,d,a)==False or InTrianble(c,d,a,b)==False or InTrianble(d,a,b,c)==False:
  print("No")
else:
  print("Yes")