l=int(input())
num1=l
num2=0
while(l>0):
    dig=l%10
    num2=num2*10+dig
    l=l//10
if(num1==num2):
    print("yes")
else:
    print("no")
