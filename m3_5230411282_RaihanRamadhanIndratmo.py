class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga


class Daftarmenu:
    def __init__(self):
        self.makanan = []
        self.minuman = []
        self.menuDefault()

    def tambahItem(self, jenis, nama, harga):
        item = Menu(nama, harga)
        if jenis == "makanan":
            self.makanan.append(item)
        elif jenis == "minuman":
            self.minuman.append(item)

    def menuDefault(self):
        default_makanan = [
            ("NASIIIUUU BAKAR", 12000),
            ("MIE SKIN PEDAS", 8000),
            ("DAGING WAHYU A7", 27000)
        ]
        default_minuman = [
            ("ES TEH ANGET", 5000),
            ("KOPI DIPETENGI", 7000),
            ("TEH TUBRUK", 8000)
        ]

        for nama, harga in default_makanan:
            self.tambahItem("makanan", nama, harga)

        for nama, harga in default_minuman:
            self.tambahItem("minuman", nama, harga)

    def nampilkanMenu(self, jenis):
        items = self.makanan if jenis == "makanan" else self.minuman
        print(f"\n=== DAFTAR {jenis.upper()} ===")
        if not items:
            print(f"Belum ada menu {jenis}.")
        else:
            for i, item in enumerate(items, 1):
                print(f"{i}. {item.nama} - Rp{item.harga}")


def inputItem(jenis):
    nama = str(input(f"Masukkan nama {jenis}: "))
    harga = int(input(f"Masukkan harga {jenis}: "))
    return nama, harga


def main():
    daftarMenu = Daftarmenu()

    while True:
        print("\n===== RESTORAN GENJEH 07 =====")
        print("1. LIHAT DAFTAR MAKANAN")
        print("2. LIHAT DAFTAR MINUMAN")
        print("3. TAMBAH MENU")
        print("0. KELUAR")

        inputMenu = input("Masukkan pilihan Anda [1-3], 0 Keluar : ")

        if inputMenu == "1":
            daftarMenu.nampilkanMenu("makanan")
        elif inputMenu == "2":
            daftarMenu.nampilkanMenu("minuman")
        elif inputMenu == "3":
            while True:
                print("\n=== MAU TAMBAH APA ? ===")
                print("1. MAKANAN")
                print("2. MINUMAN")
                print("0. KEMBALI KE MENU UTAMA")

                subMenu = input("Masukkan pilihan Anda: ")

                if subMenu == "1":
                    nama, harga = inputItem("makanan")
                    daftarMenu.tambahItem("makanan", nama, harga)
                    print("Menu makanan berhasil ditambahkan!")
                elif subMenu == "2":
                    nama, harga = inputItem("minuman")
                    daftarMenu.tambahItem("minuman", nama, harga)
                    print("Menu minuman berhasil ditambahkan!")
                elif subMenu == "0":
                    break
                else:
                    print("Error. Pilihan tidak tersedia.")
        elif inputMenu == "0":
            print("Terima kasih! Program berakhir.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


main()
