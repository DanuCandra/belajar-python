# input dari user

# data yang dimasukkan pasti string
data = input("Masukkan data: ")

print("data = ", data,"type = ",type(data))

# jika kita ingin mengambil int, maka

angka = float(input("masukkan angka: "))
angka = int(input("masukkan angka: "))

print("data = ", angka, "type = ", type(angka))

# bagaimana dengan boolean
binner = bool(int(input("Masukkan nilai boolean: ")))

print("data = ", binner, "type = ", type(binner))