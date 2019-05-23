kani=int(input())
suji=int(input())
rubi=int(input())
if((kani>=suji)and (kani>=rubi)):
    print(kani)
elif((rubi>=kani)and (rubi>=suji)):
    print(rubi)
else:
    print(suji)
