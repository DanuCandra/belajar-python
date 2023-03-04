
print("\nPROGRAM KONVERSI TEMPERATUR\n")


fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))
print("suhu adalah ", fahrenheit, "Fahrenheit")

# celcius
celcius = (5/9 * (fahrenheit -32))
print("suhu dalam celcius adalah ", celcius, "Celcius")

# reamur
reamur = (4/9 * (fahrenheit - 32))
print("suhu dalam reamur adalah ", reamur, "Reamur")

# kelvin
kelvin = (5/9 * (fahrenheit -32)) + 273
print("suhu dalam kelvin adalah ", kelvin, "Kelvin")