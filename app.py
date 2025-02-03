import os

# Dosya yolu belirle (Relative Path)
dosya_yolu = "./ogrenci_notlari.txt"

# Kullanıcıdan notları al
matematik = float(input("Matematik notunuzu girin: "))
fizik = float(input("Fizik notunuzu girin: "))
kimya = float(input("Kimya notunuzu girin: "))

# Ortalama hesapla
ortalama = (matematik + fizik + kimya) / 3

# Sonucu belirle
if ortalama >= 50:
    sonuc = "Geçti"
else:
    sonuc = "Kaldı"

# Dosyaya yaz
with open(dosya_yolu, "w") as dosya:
    dosya.write(f"Matematik: {matematik}\n")
    dosya.write(f"Fizik: {fizik}\n")
    dosya.write(f"Kimya: {kimya}\n")
    dosya.write(f"Ortalama: {ortalama:.2f}\n")
    dosya.write(f"Sonuç: {sonuc}\n")
    
# Dosyadan oku
with open(dosya_yolu, "r") as dosya:
    print(dosya.read())
