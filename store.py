print("welcome to my store")
s_name=input("enter store name : ")
if(s_name=="jagriti" or s_name=="JAGRITI"):
    print("""1.MOBILE \n 2.LAPTOP""")
    ch=input("enter your choice : ")
    if(ch=="MOBILE" or ch=="mobile"):
        print("""you having two brands right now
              1.REALME
              2.IPHONE""")
        brand=input("enter your brand : ")
        if(brand=="realme" or brand=="REALME"):
            print("PRICE WILL BE : 100000")
        elif(brand=="IPHONE" or brand=="iphone"):
            print("PRICE WILL BE : 50000")
        else:
            print("wrong brand entered")
    elif(ch=="laptop" or ch=="LAPTOP"):
        print("""you having two brands right now
              1.HP
              2.ASUS""")
        brand=input("enter your  : ")
        if(brand=="HP" or brand=="hp"):
            print("PRICE WILL BE : 100000")
        elif(brand=="asus" or brand=="ASUS"):
            print("PRICE WILL BE : 200000")
        else:
            print("wrong brand entered")
    else:
        print("wrong input")
else:
    print("wrong input")

