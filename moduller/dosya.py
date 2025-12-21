

ad = "Efekan"
tc = 20222241528
print(type(tc))
print(type(ad))
#  veri tipi, sınıf ve nesne kavramı
ogrenciler = ["Hüseyin","Emre","Bartu"]
print(type(ogrenciler))


# ogrenci = "Emir"
# ogrenci.ad = "Emir"
# ogrenci.nu = "452"


class Ogrenci():
    ad = "--"
    nu = "00"


ogrenci1 = Ogrenci()
ogrenci1.ad = "Emir"
ogrenci1.nu = 888
print(ogrenci1.ad, ogrenci1.nu)
print(type(ogrenci1))

# nesne tanımlama
class Ogrenci():
    def __init__(self,adi,num):
        self.ad = adi
        self.nu = num


# ogrenci1 = Ogrenci()
# ogrenci1.ad = "Emir"
# ogrenci1.nu = 888
ogrenci1 = Ogrenci("Ahmet",666)


print(ogrenci1.ad, ogrenci1.nu)
print(type(ogrenci1))

# dosya işlemleri/dosya oluşturma
open("deneme.txt","w")

# dosya oluşturma
for a in range(10):
    open(f"deneme{a}.txt","w")

# dosyaya bilgi yazma
open("deneme.txt","w").write("abcd")

# dosyaya bilgi yazma
dosya = open("deneme.txt","w")
# w modunda dosya yoksa oluşur
# dosya varsa da içindekiler silinir.
dosya.write("merhaba")

# dosyaya bilgi ekleme
dosya = open("deneme.txt","a")
# a modunda dosya yoksa oluşur
# dosya varsa da içindekiler silinmez.
# mevcut olanlara eklenir.
dosya.write("\nnasılsın")


# GÖREV:
# klavyeden girilen ad ve telefon bilgilerini
# dosyaya alt alta yazan bir program yapın.

# klavyeden girilen ad ve telefon bilgilerini dosyaya kaydetme
dosya = open("rehber.dat","a")
print("KAYIT EKRANI")
ad = input("Ad giriniz:")
nu = input("Telefon giriniz:")


dosya.write(f"\n{ad}#{nu}")

# dosyadan verileri okuma
dosya = open("rehber.dat") #dosya modu yazılmazsa r (read) modunda açar
print(" KAYIT LİSTESİ ")
print("===============")
okunan = dosya.read()
print(okunan)


# GÖREV:
#

# dosyadan verileri okuma
dosya = open("rehber.dat") #dosya modu yazılmazsa r (read) modunda açar
print(" KAYIT LİSTESİ ")
print("Adı\t\tTelefonu")
print("==========\t==========")
# okunan = dosya.read()
okunan = dosya.readlines()
for a in okunan:
    # satir = a.split("#")
    satir = a.strip().split("#") # strip ile alt satır karakterleri vs silinir.
print(satir[0],"\t",satir[1])

# farklı yerlerdeki dosyalardan verileri okuma
# dosya = open("h04_2 dosya islemleri/deneme.txt") # klasör içindekileri / yazarak açabiliriz.
# dosya = open("deneme.txt")
dosya = open("c:/deneme11.txt") # c: sürücü adı olarak kullanılır.
print(" KAYIT LİSTESİ ")


okunan = dosya.read()
print(okunan)
# hata kontrolü
try:
    dosya = open("c:/Windows/directx65464.log") # c: sürücü adı olarak kullanılır.
    print(" KAYIT LİSTESİ ")
    okunan = dosya.read()
    print(okunan)
except:
    print("hata oluştu")



# hata kontrolü
try:
    dosya = open("c:/Windows/directx65464.log") # c: sürücü adı olarak kullanılır.
    print(" KAYIT LİSTESİ ")
    okunan = dosya.read()
    print(okunan)
except Exception as hata:
    print("hata oluştu")
    print("Hata:", hata)

# read ile istenilen miktarda okuma
d = open("rehber.dat","r", encoding="utf8")
gelen = d.read(8)
print(gelen)
gelen = d.read(5)
print(gelen)

# read ile istenilen miktarda okuma
d = open("rehber.dat","r", encoding="utf8")
gelen = d.read(8)
print(gelen)
gelen = d.read(5)
print(gelen)
gelen = d.readline()
print(gelen)
gelen = d.readline()
print(gelen)
gelen = d.readline()
print(gelen)