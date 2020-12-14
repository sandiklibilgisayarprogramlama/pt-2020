# https://www.programiz.com/python-programming/online-compiler/

# tekli yorum satırı xv  sfsd sdf sdf sdf sdf sdf sdf
    
"""
çoklu 

yorum 

satırı

IndentationError: unexpected indent
başlangıçtaki boşlukları kontrol et, yanlışın var.

SyntaxError: unexpected EOF while parsing
dil yazımında bir hata var, parantez virgül kontrolü yapın

NameError: name 'ondalikliSayi' is not defined
degisken yok, tanımlamaları kontrol edin.
"""

"""
veritipleri
isim   -  kısaltma
integer - int -> tam sayı
string - str -> karakter dizisi, kelimeler
float - float -> ondalıklı sayılar
boolean - bool -> True, False ifadeleri

type(degiskenIsmi)
"""
sayi=10
boolD=True
ondalikliSayi=10.2
strD="ahmet"
print(type(strD))

"""
Soru: 15 ve 20 sayılarını toplayan ve ekrana yazan
programı kodlayınız.

Alg:
A1: Başla
A2: toplam=15+20
A3: toplamı ekrana yaz
A4: Bitir
toplam = 15+20
print(15," ile ",20," nin toplam sonucu: ",toplam)


A1: Başla
A2: sayi1=15
A3: sayi2=20
A4: toplam=15+20
A5: toplamı ekrana yaz
A6: Bitir
"""

sayi1=15
sayi2=20
print(sayi1," ile ",sayi2," nin toplam sonucu: ",(sayi1+sayi2))

print(15," ile ",20, "nin toplamı : ",(15+20))

"""
Ör: 10 un karesini alan programı kodlayınız.
"""

print(10, "un karesi :",(10**2))

"""
ör: x^2+y^3+3x-(9*y)-90 denklemini x=3 ve y=12 için çözen programı kodlayınız.

"""
x=3
y=12
sonuc=x**2+y**3+3*x-(9*y)-90
print("sonuc :") 
print(sonuc)