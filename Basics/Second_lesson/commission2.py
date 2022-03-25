city= input()
sales= float (input())
commission = 0
if 0 <= sales <= 500:
    if city == "Sofia":
        commission=0.05
    if city == "Varna":
        commission=0.045
    if city == "Plovdiv":
        commission=0.055
elif 500 <= sales <= 1000:
    if city == "Sofia":
        commission = 0.07
    if city == "Varna":
        commission = 0.075
    if city == "Plovdiv":
        commission = 0.08
elif 1000 <= sales <= 10000:
    if city == "Sofia":
        commission = 0.08
    if city == "Varna":
        commission = 0.1
    if city == "Plovdiv":
        commission = 0.12
elif sales > 10000:
    if city == "Sofia":
        commission = 0.12
    if city == "Varna":
        commission = 0.13
    if city == "Plovdiv":
        commission = 0.145
if commission == 0:
    print ("error")
else :
    commission = sales * commission
    print (f"{commission: .2f}")