def main(a,b,c):
    
    if a>0 : a=1 
    else : a=0
    if b>0 : b=1 
    else: b=0
    if c>0 : c=1 
    else: c=0
    ans1=a+b+c
    ans2=3-ans1
    if ans1>ans2 : 
        return "there are a lot of positive numbers" ,ans1
    elif ans2>ans1 : 
        return "there are a lot of negative numbers" ,ans2

print(main(0,-2,1)) 



    