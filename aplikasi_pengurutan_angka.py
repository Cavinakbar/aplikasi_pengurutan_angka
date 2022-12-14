#belajar dengan membuat progam dengan list
print("PROGRAM MENENTUKAN ANGKA GANJIL DAN GENAP DARI DATA YANG DIBERIKAN")
print("""
INGAT JIKA INGIN MEMASUKAN RANGE SYARATNYA ADALAH
INGIN MEMASUKKAN ANGKA 1 - 10 MAKA TULIS DI RANGE PERTAMA ADALAH 1 DAN DI RANGE KEDUA ADALAH 10
""")
inputuser1 = int(input("Masukkan range pertama: "))
inputuser2 = int(input("Masukkan range kedua:   "))

mengurutkan_list = [x for x in range(inputuser1,inputuser2) if x%2 == 0 ]
print(f"ANGKA GENAP:{mengurutkan_list}")

mengurutkan_list = [x for x in range(inputuser1,inputuser2) if x%2 != 0 ]
print(f"ANGKA GANJIL:{mengurutkan_list}")

print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")