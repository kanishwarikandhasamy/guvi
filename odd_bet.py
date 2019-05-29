kani=int(input())
suji=int(input())
for i in range(kani+1,suji):
    if(i%2==0):
        continue
    else:
        print(i," ",end="")
