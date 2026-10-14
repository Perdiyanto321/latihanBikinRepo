def input_int(pesan, pilihan=None):
    while True:
        try:
            x = int(input(pesan))
            if pilihan and x not in pilihan:
                print("Pilihan tidak tersedia")
                continue
            return x
        except:
            print("Input harus angka")

def input_float(pesan):
    while True:
        try:
            return float(input(pesan))
        except:
            print("Input harus angka")

def perhitungan():
    n = input_int("Masukkan jumlah bilangan: ")
    angka = input_float("Masukkan angka ke-1: ")
    hasil = angka
    for i in range(2, n + 1):
        op = input("Masukkan operator (+ - * /): ")
        while op not in ["+", "-", "*", "/"]:
            op = input("Masukkan operator (+ - * /): ")
        angka = input_float(f"Masukkan angka ke-{i}: ")
        if op == "+":
            hasil += angka
        elif op == "-":
            hasil -= angka
        elif op == "*":
            hasil *= angka
        elif op == "/":
            while angka == 0:
                angka = input_float("Tidak boleh 0, masukkan ulang: ")
            hasil /= angka
    print("Hasil:", hasil)

def bmi():
    bb = input_float("Masukkan berat badan (kg): ")
    tb = input_float("Masukkan tinggi badan (cm): ") / 100
    nilai = bb / (tb * tb)
    print("BMI:", round(nilai, 2))
    if nilai < 18.5:
        print("Kurus")
    elif nilai < 25:
        print("Normal")
    elif nilai < 30:
        print("Gemuk")
    else:
        print("Obesitas")

def konversisuhu():
    menu = input_int("1.Celcius 2.Fahrenheit 3.Reamur 4.Kelvin: ", [1,2,3,4])
    nilai = input_float("Masukkan suhu: ")
    if menu == 1:
        print("F:", nilai * 9/5 + 32)
        print("R:", nilai * 4/5)
        print("K:", nilai + 273.15)
    elif menu == 2:
        print("C:", (nilai - 32) * 5/9)
        print("R:", (nilai - 32) * 4/9)
        print("K:", (nilai - 32) * 5/9 + 273.15)
    elif menu == 3:
        print("C:", nilai * 5/4)
        print("F:", nilai * 9/4 + 32)
        print("K:", nilai * 5/4 + 273.15)
    else:
        print("C:", nilai - 273.15)
        print("F:", (nilai - 273.15) * 9/5 + 32)
        print("R:", (nilai - 273.15) * 4/5)

def bangundatar():
    menu = input_int("1.Persegi 2.Persegi Panjang 3.Segitiga 4.Lingkaran: ", [1,2,3,4])
    pilih = input_int("1.Luas 2.Keliling: ", [1,2])
    if menu == 1:
        s = input_float("Sisi: ")
        print(s*s if pilih==1 else 4*s)
    elif menu == 2:
        p = input_float("Panjang: ")
        l = input_float("Lebar: ")
        print(p*l if pilih==1 else 2*(p+l))
    elif menu == 3:
        if pilih == 1:
            a = input_float("Alas: ")
            t = input_float("Tinggi: ")
            print(0.5*a*t)
        else:
            a = input_float("Sisi A: ")
            b = input_float("Sisi B: ")
            c = input_float("Sisi C: ")
            print(a+b+c)
    else:
        r = input_float("Jari-jari: ")
        print(3.14*r*r if pilih==1 else 2*3.14*r)

def konversimasa():
    print("\n=== KONVERSI MASSA ===")
    print("1. Kilogram ke Gram")
    print("2. Gram ke Kilogram")

    pilihan = input("Pilih: ")
    nilai = input_angka("Masukkan nilai: ")

    if pilihan == "1":
        print("Hasil:", nilai * 1000, "g")
    elif pilihan == "2":
        print("Hasil:", nilai / 1000, "kg")
    else:
        print("Pilihan tidak valid")

def konversipanjang():
    print("\n=== KONVERSI PANJANG ===")
    print("1. Meter ke Kilometer")
    print("2. Kilometer ke Meter")

    pilihan = input("Pilih: ")
    nilai = input_angka("Masukkan nilai: ")

    if pilihan == "1":
        print("Hasil:", nilai / 1000, "km")
    elif pilihan == "2":
        print("Hasil:", nilai * 1000, "m")
    else:
        print("Pilihan tidak valid")


while True:
    print("\nMENU")
    print("1.Perhitungan")
    print("2.Konversi Suhu")
    print("3.Bangun Datar")
    print("4.BMI")
    print("5.konversi masa")
    print("6.konversi panjang")
    print("0.Keluar")
    pilih = input_int("Pilih menu: ", [0,1,2,3,4,5,6])
    if pilih == 0:
        break
    elif pilih == 1:
        perhitungan()
    elif pilih == 2:
        konversisuhu()
    elif pilih == 3:
        bangundatar()
    elif pilih == 4:
        bmi()
    elif pilih == 5:
        konversimasa()
    elif pilih == 6:
        konversipanjang()
