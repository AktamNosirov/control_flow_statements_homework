def main(a,b,c):
    ans1=0
    ans2=0
    if a>0 : ans1+=1 
    else: ans2+=1 
    if b>0 :ans1+=1 
    else: ans2+=1 
    if c>0 : ans1+=1 
    else: ans2+=1 
    d=a+b+c
    if ans1>ans2 :
        return "there are a lot of positive numbers", ans1,
    if ans1<ans2: 
        return "there are a lot of negative numbers" ,ans2
print(main(1,-2,-3))


