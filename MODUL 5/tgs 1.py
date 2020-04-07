class MhsTIF(object):
   
    def __init__(self,nama,NIM,asal,saku):
        self.nama = nama
        self.NIM = NIM
        self.asal = asal
        self.saku = saku
        
c0 = MhsTIF ('Japar','L200180001','Sukoharjo', 240000)
c1 = MhsTIF ('Ujang','L200180010','Sragen', 230000)
c2 = MhsTIF ('Bejo','L200180002','Surakarta', 250000)
c3 = MhsTIF ('Dian','L200180004','Surakarta', 230000)
c4 = MhsTIF ('Ipul','L200180005','Boyolali', 240000)
c5 = MhsTIF ('Dudung','L20018006','Salatiga', 250000)
c6 = MhsTIF ('Rudi','L200180007','Klaten', 245000)
c7 = MhsTIF ('Adi','L20018008','Wonogiri', 245000)
c8 = MhsTIF ('Dadang','L200180009','Klaten', 245000)
c9 = MhsTIF ('Tuti','L2001800011','Karanganyar', 270000)
c10 = MhsTIF ('Agung','L200180012','Purwodadi', 265000)
Mhs = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def urutkan(A):
    baru = {}
    for i in range(len(A)):
        baru[A[i].nama] = A[i].NIM
    listofTuples = sorted(baru.items(), key = lambda x: x[1])
    for elemen in listofTuples :
        print(elemen[0], ":", elemen[1])
