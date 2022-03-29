open_tabs=int(input())
salary=int(input())
# ⦁	"Facebook" -> 150 лв.
# ⦁	"Instagram" -> 100 лв.
# "Reddit" -> 50 лв.
facebook=150
instagram=100
reddit=50
for tab in range(open_tabs):
    website=input()
    if website=="Facebook":
        salary-= facebook
    elif website == "Instagram":
        salary -= instagram
    elif website == "Reddit":
        salary-=reddit
if salary <=0:
    print("You have lost your salary.")
elif salary > 0:
    print (salary)