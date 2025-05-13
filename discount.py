# give the discount according to the purchase amount
# 0-1000 --> give 5% discount
# 1000-5000--> give 10%
# 5000-10000-->15%
# above 10000-->20%

num=int(input("enter your purchase amount"))
if(num>0 and num<=1000):
    print("you got a 5% discount")
    print("your amount is",(num-(num*5)/100))

elif(num>1000 and num<=5000):
    print("you got a 10% discount")
    print("your amount is",(num-(num*10)/100))
    
    
elif(num>5000 and num<=10000):
    print("you got a 15%" \
    " discount")
    print("your amount is",(num-(num*15)/100))

elif (num<=1000):
    print("you got a 25% discount")
    print("your amount is",(num-(num*25)/100))
else:
    print("invalid input")
    

