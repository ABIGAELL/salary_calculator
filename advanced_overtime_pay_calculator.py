ans=raw_input("did you work overtime this week?")
if ans=="no":

    hours=float(input("how many hours did you work for?"))
    rate=float(input("what rate per hour do you get paid?"))
    pay= hours*rate
    print("your pay for this week is ",int(pay))
else:
    hours=float(input("how many hours did you work for?"))
    rate=float(input("what rate per hour do you get paid?"))

    hours=hours-40
    overtimepay= rate*1.5
    overtimepay=overtimepay*hours
    normalpay=40*rate
    pay=normalpay+overtimepay

    print("your pay for this week is ",int(pay),"with an overtime pay of ",float(overtimepay))
