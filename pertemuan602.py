import math

# Fungsi untuk menghitung hipotenusa
def hitung_hipotenusa(a, b):
    c = math.sqrt(a**2 + b**2)  # Rumus Pythagoras
    return c

# Nilai a dan b
a = 7
b = 5

# Menghitung hipotenusa
c = hitung_hipotenusa(a, b)

# Menampilkan hasil
print(f"Panjang hipotenusa adalah: {c}")


# Daftar bilangan
bilangan = [34, 20, 67, 91, 29, 42, 77, 39, 84, 43, 94]

# Menghitung nilai maksimum dan minimum
max_bilangan = max(bilangan)
min_bilangan = min(bilangan)

# Menampilkan hasil
print(f"Nilai maksimum: {max_bilangan}")
print(f"Nilai minimum: {min_bilangan}")
