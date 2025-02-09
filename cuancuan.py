uang_disimpan = 20_000_000  
target = 40_000_000  
bunga = 0.1  
tahun = 0  

while uang_disimpan < target:  
    uang_disimpan *= 1 + bunga  # Menggunakan faktor pertumbuhan  
    tahun += 1  

print(f"Waktu yang dibutuhkan adalah {tahun} tahun")  
