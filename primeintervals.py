u,v=map(int,input().split())
for a in range(u+1,v):
  if(a>1):
      for b in range(2,a):
          if(a%b==0):
              break
      else:
          print(a,end=' ')
