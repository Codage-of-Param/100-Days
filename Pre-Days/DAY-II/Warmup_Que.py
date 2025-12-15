def Check_coupon(x,y,prices):
    cost = sum(prices)
    print(f"\nTotal Cost before applying coupon is {cost}")

    discPrice = []
    
    for i in range(len(prices)):
        applyDisc = prices[i] - y
        if(applyDisc<0):
            discPrice.append(0)
        else:
            discPrice.append(applyDisc)
     
    discPriceSum = sum(discPrice)
    discCost = x + discPriceSum
    print(f"Total Cost after applying coupon is {discCost}")
    
    if(discCost > cost):
        return False
    elif(discCost == cost):
        return False
    else:
        return True  

n = int(input("\nEnter total items : "))
x = int(input("Enter Coupon price : "))
y = int(input("Enter discount price: "))
prices = []
i = 0

print("\n")
while (n!=0):
	price = int(input(f"Enter price of item {i+1} : "))
	prices.append(price)
	n = n-1
	i = i+1

valid = Check_coupon(x,y,prices)

if(valid==True):
    print("\nYou can apply COUPON, Its on your benifit.\n")
else:
    print("\nYou can't apply COUPON, Its not on your benifit.\n")