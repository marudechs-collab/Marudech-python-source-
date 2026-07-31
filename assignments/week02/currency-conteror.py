print("Select currency")
print("1. THB TO USD")
print("2. USD TO THB")
choice=int(intput("THB to USD or USD to THB"))

if choice==1:
    print("THB TO USD")
    thb=float(input("Enter your THB"))
    usd=thb/32
    print("Your USD =", usd)
elif choice==2:
    print("USD TO THB")
    usd=float(input("Enter your USD"))
    thb=usd*32
    print("Your THB =", thb)
else:
    print("wrong choice")