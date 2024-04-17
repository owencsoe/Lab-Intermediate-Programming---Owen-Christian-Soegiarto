print("=============================================")
print ("| Month  |  Amount of Money paid to the bank")    
print("=============================================")

bunga05=round(10000000/12)+(10000000*0.005)
bunga1=round(10000000/12)+(10000000*0.01)

for i in range(1,7):
     print("|", i*1,"| Rp.",bunga05,"                             |")
for i in range(7,13):
     print("|", i*1,"| Rp.",bunga1,"                             |")

print("Total payment = Rp.", (bunga05*6)+(bunga1*6)+10000000)
