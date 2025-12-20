birler_deger = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar_deger = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

def okunus(x):
    birler = x % 10
    onlar = x // 10
    sonuc = onlar_deger[onlar] + " " + birler_deger[birler]
    return sonuc

a = int(input("İki basamaklı bir sayı giriniz: "))
print(okunus(a)) 
