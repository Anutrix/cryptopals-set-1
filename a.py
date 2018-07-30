import codecs
s=input()
res=codecs.encode((codecs.decode(s,"hex")), "base64")
print(res)