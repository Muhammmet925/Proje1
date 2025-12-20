def cizimmenu():
    print("Ana Menü")
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   çizimler menÜ \033[1;32;40m   ║")
    print("║                     ║")
    print("║  1-KARE             ║")
    print("║  2-Üçgen            ║")
    print("║  3-desen            ║")
    print("║  4-pikachu          ║")
    print("║  5-bayrak           ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
    secim=input("Seçiminiz:")
    if secim=="1" or secim=="KARE":
        print("KARE seçtiniz.")
        import moduller.cizimler_kare        
    elif secim=="2" or secim=="Üçgen":
        print("Üçgen seçtiniz.")
        import moduller.cizimler_ucgen
        moduller.cizimler_ucgen.ucgen()
    elif secim=="3" or secim=="desen":
        print("Desen seçtiniz.")
        import moduller.cizimler_desen
        moduller.cizimler_desen 
    elif secim=="4" or secim=="pikachu":
        print("Pikachu seçtiniz.")
        import moduller.cizimler_pikachu
        moduller.cizimler_pikachu.main()
    elif secim=="5" or secim=="bayrak":
        print("bayrak seçtiniz.")
        import moduller.cizimler_bayrak
        moduller.cizimler_bayrak
    elif secim=="6" or secim=="çıkış":
        print("Çıkış yapıldı.")
        import sys  
        sys.exit()
    else:
        print("Geçersiz seçim.")    
    # cizimmenu()

# cizimmenu()  