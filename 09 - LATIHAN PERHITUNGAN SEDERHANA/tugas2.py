print("\nPROGRAM KONVERSI TEMPERATUR\n")

kelvin = float(input("Masukkan suhu dalam kelvin : "))
print("suhu adalah ", kelvin, "kelvin")

# celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah ", celcius, "Celcius")

# reamur
reamur = (4/5*(kelvin-273))
print("suhu dalam reamur adalah ", reamur, "Reamur")

fahrenheit = ((9/5)* celcius)+32
print("suhu dalam fahrenheit adalah ", fahrenheit, "fahrenheit")