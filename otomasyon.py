
kadi="eren"
sifre="123"
girilen_kadi=str(input("    ÖĞRENCİ NOT OTOMASYON SİSTEMİ   \nKullanıcı Adınızı Giriniz : "))
girilen_sifre=str(input("Şifrenizi Giriniz : "))

if (girilen_kadi==kadi):
     if(girilen_sifre==sifre):
         print("ÖĞRENCİ NOT OTOMASYON SİSTEMİNE HOŞGELDİNİZ  ")
     else:
         print("ŞİFRE YANLIŞ")
         exit()
else:
    print("KULLANICI ADI YANLIŞ LÜTFEN TEKRAR DENEYİNİZ ")
    exit()

matvize=int(input("MATEMATİK  DERSİ VİZE NOTU GİRİNİZ :"))
matfinal=int(input("MATEMATİK DERSİ FİNAL NOTU GİRİNİZ :"))
ortalama=(matvize*30 + matfinal*70)/100
matort=(matvize*30 + matfinal*70)/100

if 79.50 <= matort <= 100:
    matort = "AA İLE GEÇTİ"
elif 74.50 <= matort <= 79.49:
    matort = "BA İLE GEÇTİ"
elif 69.50 <= matort <= 74.49:
    matort = "BB İLE GEÇTİ"
elif 64.50 <= matort <= 69.49:
    matort = "CB İLE GEÇTİ"
elif 59.50 <= matort <= 64.49:
    matort = "CC İLE GEÇTİ"
elif 54.50 <= matort <= 59.49:
    matort = "DC İLE KOŞULLU GEÇTİ"
elif 49.50 <= matort <= 54.49:
    matort = "DD İLE KOŞULLU GEÇTİ"
elif 39.50 <= matort <= 49.49:
    matort = "FD İLE KALDI"
elif 0 <= matort <= 39.49:
    print("FF İLE KALDI ")
else:
    print("HATALI NOT GİRDİNİZ LÜTFEN TEKRAR DENEYİNİZ" )

print("MATEMATİK  DERSİNİN ORTALAMASI =",ortalama,matort)


isletmevize=int(input("İŞLETME DERSİ VİZE NOTU GİRİNİZ :"))
isletmefinal=int(input("İŞLETME DERSİ FİNAL NOTU GİRİNİZ :"))
ortalama=(isletmevize*30 + isletmefinal*70)/100
isletmeort=(isletmevize*30 + isletmefinal*70)/100
if 79.50 <= isletmeort <= 100:
    isletmeort = "AA İLE GEÇTİ"
elif 74.50 <= isletmeort <= 79.49:
    isletmeort = "BA İLE GEÇTİ"
elif 69.50 <= isletmeort <= 74.49:
    isletmeort = "BB İLE GEÇTİ"
elif 64.50 <= isletmeort <= 69.49:
    isletmeort = "CB İLE GEÇTİ"
elif 59.50 <= isletmeort <= 64.49:
    isletmeort = "CC İLE GEÇTİ"
elif 54.50 <= isletmeort <= 59.49:
    isletmeort = "DC İLE KOŞULLU GEÇTİ"
elif 49.50 <= isletmeort <= 54.49:
    isletmeort = "DD İLE KOŞULLU GEÇTİ"
elif 39.50 <= isletmeort <= 49.49:
    isletmeort = "FD İLE KALDI"
else:
    isletmeort = "FF İLE KALDI"
print("İŞLETME DERSİNİN ORTALAMASI =",ortalama,isletmeort)

algoritmavize=int(input("ALGORİTMA DERSİ VİZE NOTU GİRİNİZ :"))
algoritmafinal=int(input("ALGORİTMA DERSİ FİNAL NOTU GİRİNİZ :"))
ortalama=(algoritmavize*30 + algoritmafinal*70)/100
algort=(algoritmavize*30 + algoritmafinal*70)/100
if 79.50 <= algort <= 100:
    algort = "AA İLE GEÇTİ"
elif 74.50 <= algort <= 79.49:
    algort = "BA İLE GEÇTİ"
elif 69.50 <= algort <= 74.49:
    algort = "BB İLE GEÇTİ"
elif 64.50 <= algort <= 69.49:
    algort = "CB İLE GEÇTİ"
elif 59.50 <= algort <= 64.49:
    algort = "CC İLE GEÇTİ"
elif 54.50 <= algort <= 59.49:
    algort = "DC İLE KOŞULLU GEÇTİ"
elif 49.50 <= algort <= 54.49:
    algort = "DD İLE KOŞULLU GEÇTİ"
elif 39.50 <= algort <= 49.49:
    algort = "FD İLE KALDI"
else:
    algort = "FF İLE KALDI"
print("ALGORİTMA DERSİNİN ORTALAMASI =",ortalama,algort)

istablovize=int(input("İŞLEM TABLOLARI DERSİ VİZE NOTU GİRİNİZ :"))
istablofinal=int(input("İŞLEM TABLOLARI DERSİ FİNAL NOTU GİRİNİZ :"))
ortalama=(istablovize*30 + istablofinal*70)/100
istabort=(istablovize*30 + istablofinal*70)/100
if 79.50 <= istabort <= 100:
    istabort = "AA İLE GEÇTİ"
elif 74.50 <= istabort <= 79.49:
    istabort = "BA İLE GEÇTİ"
elif 69.50 <= istabort <= 74.49:
    istabort = "BB İLE GEÇTİ"
elif 64.50 <= istabort <= 69.49:
    istabort = "CB İLE GEÇTİ"
elif 59.50 <= istabort <= 64.49:
    istabort = "CC İLE GEÇTİ"
elif 54.50 <= istabort <= 59.49:
    istabort = "DC İLE KOŞULLU GEÇTİ"
elif 49.50 <= istabort <= 54.49:
    istabort = "DD İLE KOŞULLU GEÇTİ"
elif 39.50 <= istabort <= 49.49:
    istabort = "FD İLE KALDI"
else:
    istabort = "FF İLE KALDI"

print("İŞLEM TABLOLARI DERSİNİN ORTALAMASI =",ortalama,istabort)

pazarlamavize=int(input("PAZARLAMA DERSİ VİZE NOTU GİRİNİZ :"))
pazarlamafinal=int(input("PAZARLAMA DERSİ FİNAL NOTU GİRİNİZ :"))
ortalama=(pazarlamavize*30 + pazarlamafinal*70)/100
pazort=(pazarlamavize*30 + pazarlamafinal*70)/100
if 79.50 <= pazort <= 100:
    pazort = "AA İLE GEÇTİ"
elif 74.50 <= pazort <= 79.49:
    pazort = "BA İLE GEÇTİ"
elif 69.50 <= pazort <= 74.49:
    pazort = "BB İLE GEÇTİ"
elif 64.50 <= pazort <= 69.49:
    pazort = "CB İLE GEÇTİ"
elif 59.50 <= pazort <= 64.49:
    pazort = "CC İLE GEÇTİ"
elif 54.50 <= pazort <= 59.49:
    pazort = "DC İLE KOŞULLU GEÇTİ"
elif 49.50 <= pazort <= 54.49:
    pazort = "DD İLE KOŞULLU GEÇTİ"
elif 39.50 <= pazort <= 49.49:
    pazort = "FD İLE KALDI"
else:
    pazort = "FF İLE KALDI"
print("PAZARLAMA DERSİNİN ORTALAMASI =",ortalama,pazort)

print ("          GENEL ORTALAMA      ")

gort=(pazarlamavize+pazarlamafinal+istablovize+istablofinal+matvize+matfinal+algoritmavize+algoritmafinal+isletmevize+isletmefinal)/10
if gort >= 49.5:
    print(gort,"ORTALAMA İLE ÖĞRENCİ BAŞARILI")
else:
    print(gort,"ORTALAMA İLE ÖĞRENCİ BAŞARISIZ")

