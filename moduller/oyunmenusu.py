def oyunmenu():
    print("Ana Menü")
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m    oyunlar   \033[1;32;40m       ║")
    print("║                     ║")
    print("║  1-Tetris           ║")
    print("║  2-kelime bilmece   ║")
    print("║  3-sayı bilmece     ║")
    print("║  4-adam asmaca      ║")
    print("║  5-tkm              ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
    secim=input("Seçiminiz:")
    if secim=="1" or secim=="Tetris":
        print(" seçtiniz.")
        import moduller.oyun_tetris    
        moduller.oyun_tetris.main()    
    elif secim=="2" or secim=="kelime bilmece":
        print("Üçgen seçtiniz.")
        import moduller.oyun_kelime
    elif secim=="3" or secim=="":
        print("Desen seçtiniz.")
        import moduller.cizimler_desen
        moduller.cizimler_desen 
    elif secim=="4" or secim=="pikachu":
        print("Pikachu seçtiniz.")
        import moduller.cizimler_pikachu
        moduller.cizimler_pikachu.main()
    elif secim=="5" or secim=="kaplan":
        print(".")
        import sys  
        sys.exit()
    else:
        print("Geçersiz seçim.")    
    # cizimmenu()

# cizimmenu()  