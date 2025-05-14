print("WELCOME TO STATE BANK OF INDIA")
ch=input("""YOUR OPTIONS ARE
      1.WITHDRAWAL
      2.DEPOSITE
      3.BALANCE CHECK : """)

if(ch=="withdrawal" or ch=="WITHDRAWAL"):
    print("your bank balance is is 10000")
    amount=int(input("enter your withdrawal amount : "))
    if(amount>0 and amount<=10000):
        print("withdrawal successfully")
        print("your current amount is",10000-amount)
    else:
        print("insufficient amount")
elif(ch=="deposite" or ch=="DEPOSITE"):
    print("your current amount is 10000")
    amount=int(input("enter your amount to deposite : "))
    if(amount>0):
        print("now current amount is ", 10000+amount)
    else:
        print("wrong input")

elif(ch=="balance enquiry" or ch=="BALANCE ENQUIRY"):
    print("your current bank amount is",10000)
else:
    print("wrong input")
