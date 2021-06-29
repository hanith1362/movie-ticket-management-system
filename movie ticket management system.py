moviename=str(input("enter the movie name:"))
priceofadult=int(input('enter the price of adult ticket:'))
priceofchild=int(input("enter the price of child ticket:"))
adultticketsold=int(input("enter the adult ticket sold:"))
childticketsold=int(input("enter the child ticket sold:"))
percentageofgrossamount=int(input("enter the percentage of gross amount:"))
percentDonation=int(input("enter the percent donation:"))
grossamount=priceofadult*adultticketsold+priceofchild*childticketsold
amountdonated=(grossamount*percentDonation)/100
netsale=grossamount-amountdonated
print("the movie name is:",moviename)
print("The number of tickets sold:",adultticketsold+childticketsold)
print("The gross amount is:",grossamount)
print("The percentage of gross amount:",percentageofgrossamount,"%")
print("The amount donated:",amountdonated)
print("The net sale is:",netsale)