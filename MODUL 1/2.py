def persegiEmpat(a,b):
    for i in range (a):
        if i == 0 or i == a-1:
            print("@"*a)
        else:
            print ("@"+" "*(b-2)+"@")
