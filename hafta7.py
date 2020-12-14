# input -> klavyeden bilgi almayı sağlayan kod
"""
girilen=input(" Sayı giriniz : ")
print(type(girilen))
"""
sayı=10 # integer
aa = 19.2 # float
g=True # bool
f="dasdas" # str

#print("merhaba" + " ali")
# pythonda iki str ifadesi arasına + koyulursa iki ifade birleştirilip yan yana yazılır.

# tip değişimi - type casting
# int(icerik) -> parantez içerisine yazılan ifadeyi tam sayıya çevirir.
# str(icerik) -> parantez içerisine yazılan ifadesi metne çevirir
# float(icerik) -> parantez içine yazılan ifadeyi ondalıklı sayıya çevirir. 


# float("10.9") -> 10.9
# float("10") -> 10.0
# int("10") -> 10 
# str(10.9) -> "10.9"
# str(10) -> "10"
#ifade="10"
#print(type(ifade))
#ifade=float(ifade)
#print(ifade)

# klavyeden girilen iki tamsayının toplamını bulan ve ekrana yazan programı kodlayınız.

x=input("1. sayıyı giriniz:")
s1=int(x)
s2=int(input("2. sayıyı giriniz:"))

toplam=s1+s2

print("toplam : "+str(toplam))