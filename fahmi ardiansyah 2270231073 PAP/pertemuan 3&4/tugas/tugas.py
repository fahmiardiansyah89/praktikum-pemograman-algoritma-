menu = "y" or "Y"
while menu == "y" or "Y":
    import datetime
    tanggal= datetime.datetime.now()

    print("========================================")
    print("=WELCOME DI WARKOP RINDU ALAM=")
    print("NAMA TOKO : FAHMI ARDIANSYAH NUGRAHA")
    print("Nama pelanggan :JAMAL")
    print("Alamat : toko jl wibawamukti4 rt17rw3")
    print("No 089663060002")
    print("==========List Menu Restoran==========")
    print(" 1. NASI GORENG GILA : Rp 15.000")
    print(" 2. MIE GORENG GILA  : Rp 12.000")
    print(" 3. ES CENDOL        : Rp 10.000")
    print(" 4. KOPI SUSU        : Rp 4.000")
    print(" 5. BUBUR KACANG IJO : Rp. 8.000")
    print("========================================")

    print("nama pelanggan:fahmi ardiansyah")
    listMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listMenu == "1":
        namaMenu= " NASI GORENG GILA "
        harga=(15000*jumlahPesanan)
        pajak= int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listMenu == "2":
        namaMenu= "MIE GORENG GILA"
        harga = (12000*jumlahPesanan)
        pajak = int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga =int(harga+pajak)
        else:
            totalHarga =int(harga+pajak)
    elif listMenu == "3":
        namaMenu= "ES CENDOL"
        harga=int(20000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga=int(harga+pajak)
    elif listMenu == "4":
        namaMenu= "KOPI SUSU"
        harga=int(4000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    elif listMenu == "5":
        namaMenu= "BUBUR KACANG IJO"
        harga=int(8000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di restoran")

    print("tanggal\t\t:",tanggal)
    print(" ------------------------------")
    print(" Menu :",namaMenu)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga :", harga)
    print(" Pajak :", pajak)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")
    menu=input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")