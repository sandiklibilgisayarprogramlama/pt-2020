"""
while koşul:
    kodlar

while döngüsünde koşullar sağlandığı takdirde içerisindeki kodlar yürütülür.


sayi= 1
while sayi< 200:
    print (sayi) 
    sayi= sayi* 2


klavyeden 0 dan küçük bir sayı girilinceye kadar ekrana 0 dan küçük gir yazan fonksiyonu yazınız.


sayi=0
while sayi>=0:
    print("0 dan küçük gir")
    sayi=int(input("bir sayi giriniz"))

while True:
    sonsuz döngü hep çalışır.


while True:
    sayi=int(input("bir sayı giriniz"))
    if sayi<0:
        break
    else:
        print("0dan küçük gir")



1-100 - 10 hak

30 -> bilmiyoruz

50 -> daha küçük bir sayı girmelisin. 9

40 -> daha küçük bir sayı girmelisin. 8

5 -> daha büyük bir sayı girmelisin. 7


* ekrana farklı sayıda * çıkar. kaç tane olduğunu tahmin ettir.

import random

aranilan = int(random.uniform(1,100))

for i in range(10,0,-1):
    print(i, "hakkınız var.")
    girilen = int(input("sayi giriniz"))
    if girilen<aranilan:
        print("daha büyük bir sayı girmeniz gerekiyor aralılan_sayı >",girilen)
    elif girilen>aranilan:
        print("daha küçük bir sayı girmeniz gerekiyor aralılan_sayı <",girilen)
    else:
        print("Tebrikler, puanınız:",i)
        break
    
    if i==1:
        print("kaybettiniz.")

# siz bunu while döngüsüne çevirin.

*******
*****
*******
****

"""
import random
print("*********************************")
print("Sayı bulma oyunu v0.1")
print("çıkmak için -1 e basınız")
print("*********************************")
simge=input("Sayısını bulmak istediğiniz simgeyi giriniz :")
simge_sayisi = int(random.uniform(10,30))
while True:
    print(simge*simge_sayisi)
    kisi_tahmin=int(input("tahmininizi giriniz"))
    if kisi_tahmin==-1:
        print("hoşçakalın")
        break
    elif kisi_tahmin==simge_sayisi:
        print("tebrikler, yeni sorunuzu hemen oluşturuyorum")
        simge_sayisi = int(random.uniform(10,30))
    elif kisi_tahmin<simge_sayisi:
        print("daha büyük bir tahminde bulunun")
    elif kisi_tahmin>simge_sayisi:
        print("daha küçük bir tahminde bulunun")
    
# çıkan şekillerin farklı sayılardan ve satırlı olmasını sağlamaya çalışın.