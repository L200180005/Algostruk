def buatNol(n,m=None):
    if(m==None):
        m=n
    print('Membuat Matriks 0 dengan Ordo '+str(n)+'x'+str(m))
    print([[0 for j in range(m)]for i in range(n)])

buatNol(3,6)
buatNol(3)

def buatIdentitas(n):
    print('Membuat Matriks Identitas dengan Ordo '+str(n)+'x'+str(n))
    print([[1 if j==i else 0 for j in range(n)]for i in range(n)])

buatIdentitas(4)
buatIdentitas(2)
