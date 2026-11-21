import json as J,os,urllib.request as Q
E=os.getenv;U=E("MAKEFUN_ENV_URL")
NB=int(E("NODE_BUDGET",4e4));MT=1e5
W=[328,1348,1460,4100,0]
T="MMMMFRNHHLMLFNMQHQOSJQWYXbebMMMM>GCGGDLLHOQQJPRRORXXL^b`BI^U+@<OFHJINSRNNQRQMPPULOTXKVYWDQROHO=EFGILIKPNLOLLJHKKJIMKSQURQKTKOSVVOPOMJKJIIHIH@IDBGIHFISNHMHJKFPKD"
D={'P':(-10,-20,-11,-9),'N':(-19,-8,12,21,19,8,-12,-21),'B':(-9,11,9,-11),'R':(-10,1,10,-1)}
D['Q']=D['K']=D['R']+D['B']
S=(0,2,1,3)
R=lambda p:(p[0][::-1].swapcase(),-p[1],S[p[3]],S[p[2]],p[4] and 119-p[4])
def V(p,j):
 if p=='R':return 1908
 t="PNBQK".index(p);r,f=9-j//10,j%10-1
 return W[t]+ord(T[t*32+r*4+min(f,7-f)])-77
def F(fn):
 q=fn.split();b=list(' '*20+' ........ '*8+' '*20);sc=0;k=0
 for ch in q[0]:
  if ch=='/':continue
  if ch.isdigit():k+=int(ch)
  else:
   j=21+k+2*(k//8);b[j]=ch;sc+=V(ch,j)if ch.isupper()else-V(ch.upper(),119-j);k+=1
 wc=('K'in q[2])*2+('Q'in q[2]);bc=('k'in q[2])*2+('q'in q[2])
 ep=ord(q[3][0])-int(q[3][1])*10+4 if q[3]!='-' else 0
 p=(''.join(b),sc,wc,bc,ep)
 return(R(p),1)if q[1]=='b'else(p,0)
def A(b,sq,by):
 for d in(9,11):
  if b[sq+d*by]=='Pp'[by<0]:return 1
 for v in'NKBR':
  for d in D[v]:
   s=sq+d
   while b[s]>' ':
    p=b[s]
    if p!='.':
     if p==(v.lower()if by<0 else v)or v in'BR'and p=='Qq'[by<0]:return 1
     break
    if v in'NK':break
    s+=d
 return 0
def G(pos):
 b,_,wc,_,ep=pos
 for i,p in enumerate(b):
  if p<'A'or p>'Z':continue
  for d in D[p]:
   j=i+d
   while b[j] not in' PNBRQK':
    if p=='P':
     if d%10==0 and(b[j]!='.'or d==-20 and(i<81 or b[i-10]!='.')):break
     if d%10 and b[j]=='.' and j!=ep:break
     if j<29:
      for pr in'NBRQ':yield(i,j,pr)
      break
    yield(i,j,'')
    if p in'PNK' or b[j]>'Z':break
    j+=d
 for k in(95,94):
  for ds,rf,bt in((k+2,98,2),(k-2,91,1)):
   if b[k]=='K'and wc&bt and b[rf]=='R'and all(b[x]=='.'for x in range(min(k,rf)+1,max(k,rf)))and all(not A(b,x,-1)for x in(k,k+(ds>k)*2-1,ds)):yield(k,ds,'')
def M(pos,mv):
 i,j,pr=mv;b,sc,wc,bc,ep=pos
 p,q=b[i],b[j];bo=list(b)
 s=V(p,j)-V(p,i)
 if q>'Z':s+=V(q.upper(),119-j)
 if p=='P':
  if j<29:s+=V(pr,j)-V('P',j)
  if j==ep:s+=V('P',119-(j+10))
 sc+=s
 bo[j]=bo[i];bo[i]='.'
 wc&=~((i==91)+(i==98)*2)
 bc&=~((j==21)+(j==28)*2)
 if p=='K':
  wc=0
  if abs(j-i)==2:
   bo[91+(j>i)*7]='.';bo[(i+j)//2]='R'
 if p=='P':
  if j<29:bo[j]=pr
  if j==ep:bo[j+10]='.'
 return R((''.join(bo),sc,wc,bc,i-10 if p=='P'and j-i==-20 else 0))
L=lambda pos:[mv for mv in G(pos)if not A((nb:=M(pos,mv)[0]),nb.index('k'),1)]
O=lambda ms,b:ms.sort(key=lambda mv:-2e5-V(mv[2],mv[1])if mv[2]else-1e5-10*V(b[mv[1]].upper(),119-mv[1])+V(b[mv[0]],mv[0])if b[mv[1]]!='.'else 0)
TT={};NN=LM=0
def Z(pos,d,a,be):
 global NN
 b,sc,*_,ep=pos
 ki=b.index('K')
 NN+=1
 if NN>LM:1/0
 q=d<=0
 if q:
  if A(b,ki,-1):
   ms=L(pos)
   z=-MT
  else:
   if sc>=be:return sc
   z=sc;a=max(a,sc)
   ms=[mv for mv in G(pos)if(b[mv[1]]!='.'or mv[1]==ep)and not A((nb:=M(pos,mv)[0]),nb.index('k'),1)]
 else:
  e=TT.get((pos,d))
  if e is not None:return e
  ms=L(pos)
  ic=A(b,ki,-1)
  if not ms:return ic*-MT
  if d>=3 and not ic and be<9e4:
   s=-Z(R(pos[:4]+(0,)),d-3,-be,-be+1)
   if s>=be:return be
  z=-MT;a0=a
 O(ms,b)
 for k,mv in enumerate(ms):
  nb=M(pos,mv)
  if q:s=-Z(nb,0,-be,-a)
  else:
   cap=b[mv[1]]!='.'or mv[1]==ep
   dd=d-2 if d>=3 and k>=3 and not cap and not mv[2] and not ic else d-1
   s=-Z(nb,dd,-a-1,-a)if k else-Z(nb,d-1,-be,-a)
   if k and s>a:s=-Z(nb,d-1,-be,-a)
  z=max(z,s);a=max(a,s)
  if a>=be:break
 if not q and a0<z<be:TT[(pos,d)]=z
 return z
def u(mv,rot):
 i,j,pr=mv
 if rot:i,j=119-i,119-j
 s=lambda x:chr(96+x%10)+chr(58-x//10)
 return s(i)+s(j)+(pr or'').lower()
def H(pa,bo):return J.load(Q.urlopen(U+pa,J.dumps(bo).encode()))
def main():
 global NN,LM
 while(g:=H("/game",{}))["status"]!="done":
  while g["status"]=="your_move":
   pos,rot=F(g["fen"])
   lg=L(pos);bm=lg[0];NN=0;LM=NB
   for d in range(1,9):
    try:
     a=-MT
     for mv in[bm]+[m for m in lg if m!=bm]:
      s=-Z(M(pos,mv),d-1,-MT,-a)
      if s>a:a=s;bm=mv
    except:break
   g=H("/move",{"game":g["game"],"move":u(bm,rot)})
main()
