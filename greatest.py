k=int(input())
s=int(input())
r=int(input())
if((k>=s)and (k>=r)):
    print(k)
elif((r>=k)and (r>=s)):
    print(r)
else:
    print(s)
