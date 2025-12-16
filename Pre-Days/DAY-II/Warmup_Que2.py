def Comparision(x,Freshness_list, Cost_list):
    Total_cost = 0
    
    for i in range(len(Freshness_list)):
        if (Freshness_list[i] >= x):
            Total_cost = Cost_list[i]+Total_cost
    
    print(f"\nTotal cost of fresh item/s is/are {Total_cost}.")

n = int(input("\nEnter total items : "))
x = int(input("Enter minimum freshness value : "))

Freshness_list = []
Cost_list = []
i=0

print("\n")

while (n!=0):
    
    Freshness = int(input(f"Enter Freshness value of item {i+1} : "))
    Freshness_list.append(Freshness)
        
    Cost= int(input(f"Enter Cost of item {i+1} : "))
    Cost_list.append(Cost)
    
    n-=1
    i+=1
    
Comparision(x,Freshness_list, Cost_list)