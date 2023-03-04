# -----0++++++5--------8+++++++++11------


# SOAL 1
inputuser = float(input("masukkan angka sesuai rules :"))
rules1 = inputuser > 0
rules2 = inputuser < 5
rules3 = inputuser > 8
rules4 = inputuser < 11

jawaban1 = rules1 and rules2 or rules3 and rules4
print("jawabannya adalah :", jawaban1)
 
# SOAL 2
inputuser = float(input("masukkan angka sesuai rules :"))
rules1 = inputuser < 0
rules2 = inputuser > 5
rules3 = inputuser < 8
rules4 = inputuser > 11

jawaban2 = rules1 or rules2 and rules3 or rules4
print("jawabannya adalah :", jawaban2)