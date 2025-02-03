matematik = float(input("Matematik notunuzu girin: "))
fizik = float(input("Fizik notunuzu girin: "))
kimya = float(input("Kimya notunuzu girin: "))

ortalama = (matematik + fizik + kimya) / 3

if ortalama >= 50:
    print(f"Tebrikler! Sınıfı geçtiniz. Ortalamanız: {ortalama:.2f}")
else:
    print(f"Maalesef, sınıfta kaldınız. Ortalamanız: {ortalama:.2f}")