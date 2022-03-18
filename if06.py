def main(a,b,c):
    if a>0 : a=1 
    else: a=0 
    if b>0 : b=1 
    else: b=0 
    if c>0 : c=1 
    else: c=0   
    ans=a+b+c
    print("there are a lot of positive numbers" ,ans)
    print("there are a lot of positive numbers" ,3-ans)
    return ans 
print(main(-1,-2,-2.3))