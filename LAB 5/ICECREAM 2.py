SalesData = {}
with open("icecream.txt", "r") as data:
    for line in data:
        if ":" in line:
            flavor, *sales = line.strip().split(":")  
            SalesData[flavor] = [float(s) for s in sales]  

flavor_totals = {flavor: sum(sales) for flavor, sales in SalesData.items()}

store_totals = [sum(sales) for sales in zip(*SalesData.values())] 

print("Sales Report:")

print("\nSales by Flavor:")
for flavor, total_sale in sorted(flavor_totals.items()):
    print(f"{flavor}: {total_sale:.2f}")

print("\nSales by Store:")
for i, store_sale in enumerate(store_totals):
    print(f"Store {i+1}: {store_sale:.2f}")