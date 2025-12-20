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
        print("kelime bilmece seçtiniz.")
        import moduller.oyun_kelime
        moduller.oyun_kelime.main()
    elif secim=="3" or secim=="sayı bilmece":
        print("sayı bilmece seçtiniz.")
        import moduller.oyun_sayı
        moduller.oyun_sayı.main()
    elif secim=="4" or secim=="adam_asmaca":
        print("adam_asmaca")
        import moduller.oyun_adam_asmaca
        moduller.oyun_adam_asmaca.main()
    elif secim=="5" or secim=="tkm":
        print("tkm")
        import moduller.oyun_tkm
        moduller.oyun_tkm.main()
    else:
        print("Geçersiz seçim.")    
    # cizimmenu()

# cizimmenu()  