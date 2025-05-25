#AMAZON WEBSITE

web=input("enter website name : ")
if(web=="amazon" or web=="AMAZON"):
    print("""1.product
          2.service""")
    ch=input("enter your choice : ")
    if(ch=="product" or ch=="PRODUCT"):
        print("""you have 2 products
              1.cloths
              2.shoes""")
        pro=input("enter your product : ")
        if(pro=="cloths" or pro=="CLOTHS"):
            print(" PRICE IS :2000")
        elif(pro=="shoes" or pro=="SHOES"):
            print("PRICE IS : 1000")
        else:
            print("wrong product enter")
    elif(ch=="service" or ch=="SERVICE"):
        print("NOT AVAILABLE")
    else:
        print("WRONG CHOICE ENTER")
else:
    print("wrong input")