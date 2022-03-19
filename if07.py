def main(a):
    if a > 0 and a%2 == 1 : 
        return "positive odd number"
    elif a > 0 and a%2 == 0 : 
        return "positive even number"
    elif a < 0 and a%2 == 1 :
        return "positive odd number"
    elif a < 0 and a%2 == 0 : 
        return "positive even number"
    else : return "the number is zero"

print(main(0))


    