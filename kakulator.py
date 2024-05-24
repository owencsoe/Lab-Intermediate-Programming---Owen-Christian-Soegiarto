def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian oleh nol"

print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

num1 = float(input("Masukkan bilangan pertama: "))
num2 = float(input("Masukkan bilangan kedua: "))

if pilihan == '1':
    print("Hasil penjumlahan:", tambah(num1, num2))
elif pilihan == '2':
    print("Hasil pengurangan:", kurang(num1, num2))
elif pilihan == '3':
    print("Hasil perkalian:", kali(num1, num2))
elif pilihan == '4':
    print("Hasil pembagian:", bagi(num1, num2))
else:
    print("Pilihan tidak valid")