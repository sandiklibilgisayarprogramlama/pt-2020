"""
5 den 150 ye kadar olan tek sayıları ekrana yazan programın algoritmasını çıkarınız.

A1: Başla
A2: sayac=5
A3: eger sayac%2==1 sayacı ekrana yaz
A4: sayac=sayac+1
A5: eğer sayac<150 ise a3' e geri dön.
A6: Bitir 

1. yol
for sayac in range(5,150):
    if sayac%2==1:
        print(sayac)

2. yol
for x in range(5,150,2);
    print(x)

for sayacdegiskeni in range(baslangic,bitis,arttırım):
    kodlar

klavyeden girilen değer kadar ekrana merhaba yazan programı kodlayınız.

tekrarSayisi=int(input("tekrar sayısını giriniz"))
for i in range(0,tekrarSayisi): # range(0,tekrarSayisi) = range(tekrarSayisi)
    print("merhaba")

*
**
***
****
***** ekrana yandaki şekli çıkaracak programı yazınız.


s="*"
s2="dünya"

print(s*15)

for i in range(1,6):
    print(i*"*")





*
--
***
***
--
*


for i in range(1,4):
    if i%2==0:
        print("-"*i)
    else:
        print("*"*i)

for i in range(3,0,-1):
    if i%2==0:
        print("-"*i)
    else:
        print("*"*i)

klavyeden girilen bir karakter ile ekrana büyük E yazacak programı kodlayınız.

*****
*
*****
*
*****



kar=input("bir karekter giriniz:")
for i in range(5):
    if i%2==0:
        print(kar*5)
    else:
        print(kar)

*****
   *
  *   
 *
*****  

00000
0   0
0   0
00000


o     o
o o   o
o  o  o
o   o o
o     o



"""