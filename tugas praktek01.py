import math

def hitung_lingkaran():
    # Meminta pengguna memasukkan jari-jari
    try:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        if jari_jari < 0:
            print("Jari-jari tidak boleh negatif.")
            return

        # Menghitung luas
        luas = math.pi * jari_jari ** 2

        # Menghitung keliling
        keliling = 2 * math.pi * jari_jari

        # Menampilkan hasil
        print(f"\nLuas lingkaran: {luas:.2f}")
        print(f"Keliling lingkaran: {keliling:.2f}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Menjalankan fungsi
hitung_lingkaran()
