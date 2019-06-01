kani=int(input())
count=0
for i in range(1,kani+1):
    if(kani%i==0):
        count=count+1
if(count>2):
        print("no")
else:
        print("yes")
