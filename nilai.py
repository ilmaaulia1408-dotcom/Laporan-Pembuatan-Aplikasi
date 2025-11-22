try:
    angka_input=int(input("masukkan bilangan (maks 7 digit):"))

    if 0 <= angka_input <= 9999999:
        
        jutaan = angka_input // 1000000
        sisa_jutaan = angka_input % 1000000

        ratusan_ribu= sisa_jutaan // 100000
        sisa_ratusan_ribu = sisa_jutaan % 100000

        puluhan_ribu = sisa_ratusan_ribu // 10000
        sisa_puluhan_ribu = sisa_ratusan_ribu % 10000

        ribuan= sisa_puluhan_ribu// 1000
        sisa_ribuan = sisa_puluhan_ribu % 1000

        ratusan= sisa_ribuan // 100
        sisa_ratusan = sisa_ribuan % 100

        puluhan = sisa_ratusan // 10
        sisa_puluhan = sisa_jutaan % 10

        satuan= sisa_jutaan % 10
        
        if angka_input >= 1000000:
            print(f"{jutaan} merupakan jutaan")
        if angka_input >=100000:
            print(f"{ratusan_ribu} merupakan ratusa ribuan")
        if angka_input >=10000:
            print(f"{puluhan_ribu} merupakan  puluhan ribu")
        if angka_input >=1000:
             print(f"{ribuan} merupakan ribuan")
        if angka_input >=100:
             print(f"{ratusan} merupakan ratusan")
        if angka_input >=10:
             print(f"{puluhan} merupakan puluhan")
        if angka_input >=1:
             print(f"{satuan} merupakan satuan")
        

    else:
        print("masukkan ulang")
except ValueError:
        print("input tidak valid!")




















