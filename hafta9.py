# seçme yapıları
"""
if koşul:
    kodlar

Klavyeden alınan değer eğer 0dan büyük ise ekrana sayı pozitif yazan programı kodlayınız.


sayi = int(input("bir sayı giriniz"))

if sayi>0:
    print(sayi,"sıfırdan büyük")

klavyeden girilen metin ali ise ekrana hoşgeldin ali yazsın


metin = input("bir isim giriniz")

if metin == "ali":
    print("hoşgeldin ",metin)


vizenin %40 ve finalin %60 etki ettiği bir sınavda öğrencinin aldığı vize ve final notlarının
ortalamasını alıp geçme notunun 60 olduğu durumda eğer öğrencinin ortalaması 60 dan büyük ve eşitse
ekrana geçti
küçükse
ekrana kaldı
yazan programı kodlayınız.



vize_not=float(input("vize notunu giriniz"))
final_not=float(input("final notunu giriniz"))
gecme_not=60
ortalama=vize_not*0.4+final_not*0.6
print("not ortalaması:",ortalama)
if ortalama>=60:
    print("dersi geçtiniz")
else:
    print("dersten kaldınız")

print("program sonlandı")
print("bitti")
print("son")

klavyeden girilen bir sayı için eğer sayı sıfırdan büyük ise ekrana 0dan büyük
eğer sayı 0a eşit ise ekrana sayı 0
eğer sayı sıfırdan küçük isede ekrana sayı 0dan küçük yazan 
programı kodlayınız.



girilen = float(input("kontrol etmek istediğiniz sayıyı giriniz:"))

if girilen>0:
    print(girilen,"sıfırdan büyük")
elif girilen<0:
    print("sıfırdan küçük")
else:
    print("sayı 0")


klavyeden girilen bir sayı eğer 4 e bölünüyor ise bu sayının bir fazlasının 3 e bölünüp bölünmediği,

sayının dörte bölünmediği durumda ise bu sayının bir eksiğinin 5 e bölünüp bölünmediğini
kontrol eden programı kodlayınız.



girilen_sayi = int(input("bir sayı giriniz:"))

if girilen_sayi%4==0:
    girilenin_bir_fazlasi=girilen_sayi+1
    if girilenin_bir_fazlasi%3==0:
        print(girilenin_bir_fazlasi," 3 e tam bölündü")
    else:
        print(girilenin_bir_fazlasi,"3 e bölünmedi")
else:
    girilenin_bir_eksigi=girilen_sayi-1
    if girilenin_bir_eksigi%5==0:
        print(girilenin_bir_eksigi," 5 e tam bölünür")
    else:
        print(girilenin_bir_eksigi," 5 tam bölünmez")


kosul1=16%5==0
kosul2=14%7==0

if kosul1:
    print("16 5 e tam bölünür. ")
elif kosul2:
    print("14 7 ye bölünür")
else:
    print("belirtilen koşul sağlanmadı")


(19>90 or 15==20) and 67-45==12
(False or False) and False
False and False
False

True and True -> True
True and False -> False
False and True -> False
False and False -> False

True or True -> True
True or False-> True
False or True -> True
False or False -> False

(67%5==2 or 13-(-13)==0) and (45%2==1 and 45/3>=15)
(True or False) and (True and True)
True and True
True

== -> is
!= -> is not


klavyeden girilen 2 sayı için birinci sayı  0 a eşit yada büyükse ve ikinci sayı sıfırdan
küçükse ekrana hoşgeldiniz yazan programı kodlayınız.

klavyeden girilen kullanıcıadı ve şifre için kullanıcıadı ahmet şifre ise ahmet123 e eşit
ise ekrana hoşgeldiniz yazan eğer ikisinden biri yanlış ise ekrana kullanıcı adı
veya şifreniz yanlış yazan programı kodlayınız.

"""

sayi1=int(input("birinci sayıyı giriniz"))
sayi2=int(input("ikinci sayıyı giriniz"))

if sayi1>=0 and sayi2<0:
    print("hoşgeldiniz")
else:
    print("koşul sağlanmıyor")


