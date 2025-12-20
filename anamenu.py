def anamenu():
    print("Ana Menü")
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m     PYTHON         \033[1;32;40m ║")
    print("║                     ║")
    print("║  1-oyun             ║")
    print("║  2-hesap makinesi   ║")
    print("║  3-çizimler         ║")
    print("║  4-not hesaplama    ║")
    print("║  5-yapay zeka       ║")
    print("║  6-çıkış            ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
    secim=input("Seçiminiz:")
    if secim=="1" or secim=="oyun":
        print("Oyun seçtiniz.") 
        import moduller.oyunmenusu
        moduller.oyunmenusu.oyunmenu()
    elif secim=="2" or secim=="hesap makinesi":
        print("Hesap makinesi seçtiniz.")
        import moduller.hesapmakinesi
    elif secim=="3" or secim=="çizimler":
        print("Çizimler seçtiniz.")
        import moduller.cizimler 
        moduller.cizimler.cizimmenu()
    elif secim=="4" or secim=="not hesaplama":
        print("Not hesaplama seçtiniz.")
        import moduller.not_hesaplama
        moduller.not_hesaplama.main()
    elif  secim=='5' or secim=='yapay zeka':
        import moduller.yapay_zeka
        moduller.yapay_zeka.main()   
    elif secim=="6" or secim=="çıkış":
        print("Çıkış yapıldı.")
        import sys
        sys.exit()
    else:
        print("Geçersiz seçim.")    
    anamenu()
 

anamenu()

