print("=============================================")
print ("| Month  |  Amount of Money paid to the bank")    
print("=============================================")
for i in range(1,7):
     print("|", i*1,"| Rp.",round(10000000*0.005),"                             |")
for i in range(7,13):
     print("|", i*1,"| Rp.",round(10000000*0.01),"                            |")

print("Total payment = Rp.", (50000*6)+(10000*6)+10000000)

