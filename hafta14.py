""" metin ve dosya işlemleri
"""

"""
\t -> tab
\n -> sonrasında geleni aşağı satıra yaz

s="ahmet \ gittik"
print(s,end="  ")
print("naber")

ad="süleyman"

eleman no 1 2 3 4 5 6 7 8
          s ü l e y m a n
indis no  0 1 2 3 4 5 6 7

karakter dizisi elemanlarını indise göre çekebiliriz


ad="süleyman"

print(ad[7])
8. elemanı getirir



print(ad[0])
1. elemanı getirir
-------------------------------------------------------------------------------
# dizinin son elemanının getirilmesi

deneme="fsıjfıwsnfısoğjrgıkngioakdaınbfpsufjkaiPDksodbsfhsıjfsofsdgdgdfgdfgdfdf"
# 1. yol
print(len(deneme))
topSayi = len(deneme)
print(deneme[topSayi-1])

# 2. yol

print(deneme[-1])


-----------------------------------------------------------------------------
ad="ismail uzun "
print(len(ad))
# substring
# 1. yol
print(ad[0],ad[1],ad[2],ad[3],ad[4],sep="")

# 2. yol

print(ad[2:])

"""

isim = "ahMET"
soyisim="UzUn"

# capitalize -> ilk harfi büyük diğerlerini küçültür
print(isim.capitalize())

# upper -> tüm karakterleri büyük yazar
print(soyisim.upper())

# lower -> tüm karakterleri küçültür
print(soyisim.lower())

# index -> içerisine verilen parçanın indisini getirir.
print(soyisim.index("z"))