#Aloysius Gonzaga Ardhian Krisna Aji
#71180298

'''membuat program penghitungan volume bangun ruang menggunakan perulangan yang terdiri dari
kubus = sisi^3, balok = p * l * t, bola = 4/3 * 3.14 * jari**3 '''

def bangunRunag():
    def menu():
        print("Penghitung Volume Bangun Ruang")
        print("1.Kubus")
        print("2.Balok")
        print("3.Bola")
        print("4.Keluar")

    def kubus(sisi):
        volumeKubus = sisi**3
        return volumeKubus

    def balok(p,l,t):
        volumeBalok = p * l * t
        return volumeBalok

    def bola(jari):
        volumeBola = 4/3 * 3.14 * jari**3
        return volumeBola

    loop = True
    while loop:
        menu()
        pilihan = int(input("Masukan pilihan anda: "))

        if pilihan == 1:
            sisi = int(input("Masukan sisi kubus yang di inginkan: "))
            print("Volume kubusnya adalah",kubus(sisi),"cm^2")
        elif pilihan == 2:
             p = int(input("Masukan panjang balok yang di inginkan: "))
             l = int(input("Masukan lebar balok yang di inginkan: "))
             t = int(input("Masukan tinggi balok yang di inginkan: "))
             print("Volume baloknya adalah",balok(p,l,t),"cm^2")
        elif pilihan == 3:
            jari = int(input("masukan Jari-Jari yang di inginkan: "))
            print("Volume bolanya adalah",bola(jari),"cm^2")
        elif pilihan == 4:
            loop = False
            print("keluar...")
        else:
            print("Yang anda inputkan salah")
    return pilihan
print (bangunRunag())

