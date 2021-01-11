# -*- coding: utf-8 -*-
kelime="merhaba"
"""
print(kelime[len(kelime)-1])
0
1
2
3
4
5
6

for i in range(0,len(kelime)):
    print(kelime[i])



for i in "naber napıyorsun?":
    if i=="n":
        print("*")
    else:
        print(i)


print("naber".replace("a","A"))


print(" 99 ahmet -".strip())

verilen metnin basındaki ve sonundaki boşlukları temizler



print(len("kelime"))
print(len("   kelime ".strip()))


print(ord("A"))

# içerisine girilen tek karakterin ascii kodunu döndürür

print(chr(97))

# içerisine girilen sayı değerinin karakterini getirir

print(bin(2))

# içerisine girilen sayı değerini binary(ikili) formata çevirir.

#1. yol
dosya = open("deneme.txt","r").read()
print(dosya)

for i in open("deneme.txt").readlines():
    print(i.capitalize(),end="")

#mode append

open("deneme.txt","a").write("naber\n")

# mode write

open("deneme.txt","w").write("naber\n")

# 2. yol

with open("deneme.txt","a") as f:
    f.write(input("bişey yaz"))
    f.close()

"""

"""
dosyada bununan bir metindeki harfler yanlış yazılmıştır. Ayşe adlı öğrenci m harfi yerine yanlışlıkla
ö harfine basmıştır. bu hatayı düzeltip dosyayı yeniden yazınız.


dosyaIcerik = open("ayseodev.txt","r").read()

yeniIcerik = dosyaIcerik.lower().replace("ö","m")

open("ayseodevv2.txt","w").write(yeniIcerik)

"""