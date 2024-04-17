while True:
    oriprice = int(input("What's the price?"))

    disc20= round(oriprice*0.2)
    disc30= round(oriprice*0.3)
    disc70= round(oriprice*0.7)

    finalprice20 = oriprice - disc20

    finalprice30 = oriprice - disc30

    finalprice70 = oriprice - disc70

    print("Price after 20% discount =", finalprice20, "$")

    print("Price after 30% discount =", finalprice30, "$")

    print("Price after 70% discount =", finalprice70, "$")
    if oriprice == 0:
        print("Thank You!")
        break