def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    if a>0 : a=1 
    else: a=0 
    if b>0 : b=1 
    else: b=0 
    if c>0 : c=1 
    else: c=0 
    return(a+b+c)
  
print(main(12,-5,-6))    
 
 