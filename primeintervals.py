u,v=map(int,input().split())
for a in range(u,v+1):
  if(a>1):
      for b in range(2,a):
          if(a%b==0):
              break
      else:
          print(a,end=' ')
