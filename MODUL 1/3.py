def jmlhhurufVokal(input):
    total=0
    voc = ['a','i','u','e','o']
    for i in input:
        if i in voc:
                total+=1
    return [len(input), total]

def jmlhhurufKonsonan (input):
    kon = ['q','w','r','t','y','p','s',
           'd','f','g','h','j','k','l',
           'z','x','c','v','b','n','m']
    b = 0
    total = 0
    for i in input:
        if i in kon:
            b +=0
    total = len(input),b
    return total
