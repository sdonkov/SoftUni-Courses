city = input()
sales = float (input())
commission = 0
if city == "Sofia" and sales >=0 and sales <= 500:
    commission = 0.05
elif city == "Sofia" and sales > 500 and sales <= 1000:
    commission = 0.07
elif city == "Sofia" and sales > 1000 and sales <= 10000:
    commission= 0.08
elif city == "Sofia" and sales >= 10000:
    commission=0.12
elif city == "Varna" and sales >= 0 and sales <= 500:
    commission = 0.045
elif city == "Varna" and sales > 500 and sales <= 1000:
    commission = 0.075
elif city == "Varna" and sales > 1000 and sales <= 10000:
    commission= 0.1
elif city == "Varna" and sales >= 10000:
    commission=0.12
elif city == "Plovdiv" and sales >=0 and sales <= 500:
    commission = 0.055
elif city == "Plovdiv" and sales > 500 and sales <= 1000:
    commission = 0.08
elif city == "Plovdiv" and sales > 1000 and sales <= 10000:
    commission= 0.12
elif city == "Plovdiv" and sales >= 10000:
    commission=0.145
elif commission == 0:
    print ("error")
else:
    commission = sales * commission
    print(f"{commission: .2f}")
commission = sales * commission

