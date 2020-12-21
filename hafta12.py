"""
break -> istenildiği takdirde döngüden çıkmaya yarayan anahtar kelimedir.

for i in range(0,10):
    print(i)
    break
output:
0
"""
"""
    klavyeden 0 girinceye kadar 100 den geriye doğru çift sayıları ekrana yazan programı kodlayınız


for i in range(100,0,-2):
    print(i)
    if(int(input("çıkmak için 0 devam etmek için herhangi bir sayı giriniz"))==0):
        break


kullanıcı tarafından girilen sayılar eğer 5 e ve ya 6 ya bölünüyorsa programdan çıkan diğer girilenleri 
ise ekrana yazan programı kodlayınız.


for i in range(100):
    sayi=int(input("bir sayı giriniz"))
    if sayi%5==0 or sayi%6==0:
        break
    else:
        print(sayi)

continue: döngüyü bir adım ilerletmek amacı ile kullanılır.



 100 den geriye doğru 5 e bölünen sayıları yazan
klavyeden dur girilince programı sonlandıran, klavyeden atla denilincede ekrana o anki yazması 
gereken sayıyı yazmayan programı yazınız.


for s in range(100,0,-5):
    girilen=input("bir kelime giriniz")
    girilen=girilen.lower()
    if girilen=="dur" :
        break
    elif girilen=="atla" :
        continue
    
    print(s)


*****

***

*





klavyeden girilen yıldız sayı değeri kadar ilk sütunu yazan altındaki çift sütunları yazmayan
programı kodlayınız.

yildiz=10

**********
*********

*******

*****

***

*




yildiz=int(input("üçgen oluşturmak için bir sayi giriniz: "))
for i in range(yildiz,0,-1):
    if i==yildiz or i%2==1:
        print("*"*i)
    else:
        print()



-*-*-*-*-*-
-*-*-*-*-
-*-*-*-
-*-*-
-*-*-*-
-*-*-*-*-
-*-*-*-*-*-
_____
(0 0)
  -
 --- 


"""


