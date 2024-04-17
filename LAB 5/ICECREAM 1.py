with open("icecream.txt","r") as my_file:
    contents = my_file.read()
    print(contents)

SalesData ={}

with open("icecream.txt", "r") as data:
    for line in data:
        if ":" in line:
            parts = line.strip().split(":")
            flavor = parts[0]
            sales = [float(part) for part in parts[1:]]
            total_sales = sum(sales)
            SalesData[flavor] = {'sales': sales, "total_sales": total_sales}

    for index in range(len(sales)):
        store = f"store{index+1}"
        if store in SalesData:
            SalesData[store]['total_sales'] += sales[index]
        else:
            SalesData[store] = {'total_sales': sales[index]}

print(SalesData)