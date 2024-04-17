#1
#a
list=[]
for i in range(1, 101):
        list.append(i)
print(list)

#b
huruf=[]
hurufa= "a"
for i in range(26):
        huruf.append(chr(ord(hurufa)+i))
print(huruf)

#2
menuRestoranA = ["bakso", "indomie", "spagetti", "es teler", "soto ayam", "nasi goreng", "nasi campur", "ramen", "es podeng", "pempek"]
findwords = ["es teler", "nasi campur"]
for word in findwords:
    if word in menuRestoranA:
            print ("Ada weh")
    else:
            print ("Gaada weh")

#3
namadata=[]
kotadata=[]

while True:
    print("\nMenu:")
    print("1. Melihat Data")
    print("2. Input Data")
    print("3. Keluar")


    pilih=int(input("1/2/3? "))

    if pilih == 1:
       print ("Nama = ", namadata,"Kota = " , kotadata)


    elif pilih == 2:
       nama=input("Nama?")
       kota=input("Kota?")
       namadata.append(nama)
       kotadata.append(kota)
       print("Saved!")

    elif pilih == 3:
       print("Ty")
       break

    else:
       print("Invalid")