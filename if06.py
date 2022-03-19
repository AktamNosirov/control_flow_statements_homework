def main(a,b,c):
    ans1=0
    ans2=0
    if a>0 : ans1+=1 
    elif a<0 :ans2+=1
    else : ans1+=0
    if b>0 : ans1+=1 
    elif b<0 :ans2+=1 
    else : ans1+=0
    if c>0 : ans1+=1
    elif c<0 :ans2+=1
    else : ans1+=0 
    if ans1>ans2 : 
        return "there are a lot of positive numbers" ,ans1
    elif ans2>ans1 : 
        return "there are a lot of negative numbers" ,ans2

print(main(0,-2,1)) 



    