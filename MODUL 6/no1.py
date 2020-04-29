from latihan2 import mergeSort
from latihan3 import quickSort
class Mahasiswa:
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.nim) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' perharinya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print('Saya baru aja makan', s, 'sambil nugas')
        self.keadaan = 'kenyang'

mh1 = Mahasiswa("Jamil", 235, "Surakarta", 250000)
mh2 = Mahasiswa("Andi", 365, "Magelang", 275000)
mh3 = Mahasiswa("Sri", 676, "Yogyakarta", 240000)
mh4 = Mahasiswa("Tedi", 737, "Karanganyar", 300000)
mh5 = Mahasiswa("Budi", 624, "Boyolali", 200000)

A = [mh1.nim, mh2.nim, mh3.nim, mh4.nim, mh5.nim]
mergeSort(A)
print(A)
