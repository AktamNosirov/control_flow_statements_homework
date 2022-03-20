def main(temp):
    if temp<0 : return "Freezing"
    elif 1<=temp and temp<=10 : return "Very Cold" 
    elif 11<=temp and temp<=20 : return "Cold"
    elif 21<=temp and temp<=30 : return "Normal"
    elif 31<=temp and temp<=40 : return "Hot"
    elif temp>=40 : return "Very Hot"
print(main(19))