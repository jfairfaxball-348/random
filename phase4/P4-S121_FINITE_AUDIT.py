from fractions import Fraction as Q
from itertools import product
def words(n): return [''.join(v) for v in product('01',repeat=n)]
def first_release(y,U):
    for t in range(len(y)):
        if any(t>=len(w) and y[:t].startswith(w) for w in U):return t
    return None
def image(x,m,U,mask):
    a=x[0];u=x[1:];cursor=0;y='';r=None
    for t in range(m):
        if r is None and any(t>=len(w) and y.startswith(w) for w in U):
            r=t;y+=a
        else:
            if r is not None and t==r+1:cursor+=1
            b=int(u[cursor]);cursor+=1
            if mask and r is not None and t>r and a=='1' and (t-r)%2==1:b^=1
            y+=str(b)
    return y
U=['00','101','1110'];tests=0
for mask in (False,True):
  for m in range(1,10):
    bins={w:[] for w in words(m)}
    for x in words(m+1): bins[image(x,m,U,mask)].append(x)
    for y,v in bins.items():
      assert len(v)==2
      r=first_release(y,U)
      assert {a[0] for a in v}==({'0','1'} if r is None else {y[r]})
      tests+=1
assert tests==2044
measures=[
 lambda s:Q(1,2**len(s)),
 lambda s:Q(1) if '1' not in s else Q(0),
 lambda s:Q(1) if '0' not in s else Q(0),
 lambda s:Q(3,4)**s.count('1')*Q(1,4)**s.count('0'),
 lambda s:(Q(1,2) if '1' not in s else Q(0))+(Q(1,2) if '0' not in s else Q(0))
]
picked=[]
for e,mu in enumerate(measures):
 s=next(s for s in words(e+6) if mu(s)>0);assert mu(s)>0;picked.append(s)
basic=sum((words(j) for j in range(4)),[])
for i,s in enumerate(basic):picked.append(s+'0'*max(1,i+9-len(s)))
N=max(map(len,picked));open_cells=sum(any(s.startswith(p) for p in picked) for s in words(N))
assert Q(open_cells,2**N)<Q(1,4)
print('PASS',tests,'exact finite fair-cap-two cylinders; 5 finite diagonal measures; 15 dense sample witnesses; mass',Q(open_cells,2**N))
