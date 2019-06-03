start,end=input().split()
start=int(start)
end=int(end)
for num in range(start+1,end):
    if(num%2!=0):
        print(num,end=" ")
