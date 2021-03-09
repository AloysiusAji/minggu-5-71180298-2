#Aloysius Gonzaga Ardhian Krisna Aji
#71180298

'''membuat program penghitungan volume bangun ruang menggunakan perulangan yang terdiri dari
kubus = sisi^3, balok = p * l * t, bola = 4/3 * 3.14 * jari**3 '''

def bangunRuang():
    def menu():
        print("Penghitung Volume Bangun Ruang Sederhana")
        print("1. Kubus")
        print("2. Balok")
        print("3. Bola")
        print("4. Exit")

    def kubus(sisi):
        volumeKubus = sisi**3
        return volumeKubus

    def balok(p, l, t):
        volumeBalok = p * l * t
        return volumeBalok
    
    def bola(jari):
        volumeBola = 4/3 * 3.14 * jari**3
        return volumeBola

    loop = True
    while loop:
        menu()
        pilihan = int(input("masukan pilihan anda: "))

        if pilihan == 1:
            sisi = int(input("Masukan panjang sisi kubus tersebut: "))
            print("Volume kubusnya adalah",kubus(sisi),"cm^2s")
        elif pilihan == 2:
            p = int(input("Masukan panjang balok tersebut: "))
            l = int(input("Masukan lebar balok tersebut: "))
            t = int(input("Masukan panjang tinggi balok tersebut: "))
            print("Volume baloknya adalah",balok(p, l, t),"cm^2s")
        elif pilihan == 3:
            jari = int(input("Masukan panjang jari-jari tersebut: "))
            print("Volume bola adalah ",bola(jari),"cm^2")
        elif pilihan == 4:
            loop = False
            print("Selesai...")
        else:
            print("Inputan yang anda masukan salah")
    return pilihan
print (bangunRuang())
