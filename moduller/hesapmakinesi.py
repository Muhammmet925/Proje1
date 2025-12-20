print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
print("║\033[1;31;40m   VEKTOREL APP  \033[1;32;40m    ║")
print("║                     ║")
print("║  1-Toplama          ║")
print("║  2-Çıkarma          ║")
print("║  3-çarpma           ║")
print("║  4-bölme            ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")
# 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
secim=input("Seçiminiz:")
if secim=="1":  
    print("Toplama seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a+b)
elif secim=="2":
    print("Çıkarma seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a-b)
if secim=="3":
    print("Çarpma seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a*b)
elif secim=="4":
    print("Bölme seçtiniz.")
    a=int(input('birinci sayıyı'))
    b=int(input("İkinci sayıyı giriniz:"))
    if b!=0:
        print("Sonuç:",a/b) 
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")
else:
    print("Geçersiz seçim.")
print("\033[0;37;40m")        