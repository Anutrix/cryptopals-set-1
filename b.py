import codecs

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr((x) ^ (y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr((x) ^ (y)) for (x, y) in zip(a, b[:len(a)])])

s1=input()
ds1=codecs.decode(s1,"hex")
s2=input()
ds2=codecs.decode(s2,"hex")
print(ds1)
print(ds2)
result = strxor(ds1,ds2)
print(codecs.encode(codecs.encode(result),"hex"))
