def get_grade(average):
    if 79.50 <= average <= 100:
        return "AA İLE GEÇTİ"
    elif 74.50 <= average <= 79.49:
        return "BA İLE GEÇTİ"
    elif 69.50 <= average <= 74.49:
        return "BB İLE GEÇTİ"
    elif 64.50 <= average <= 69.49:
        return "CB İLE GEÇTİ"
    elif 59.50 <= average <= 64.49:
        return "CC İLE GEÇTİ"
    elif 54.50 <= average <= 59.49:
        return "DC İLE KOŞULLU GEÇTİ"
    elif 49.50 <= average <= 54.49:
        return "DD İLE KOŞULLU GEÇTİ"
    elif 39.50 <= average <= 49.49:
        return "FD İLE KALDI"
    else:
        return "FF İLE KALDI"

def calculate_subject_average(vize, final):
    return (vize * 30 + final * 70) / 100

def main():
    kadi = "eren"
    sifre = "123"

    girilen_kadi = input("    ÖĞRENCİ NOT OTOMASYON SİSTEMİ   \nKullanıcı Adınızı Giriniz : ")
    girilen_sifre = input("Şifrenizi Giriniz : ")

    if girilen_kadi == kadi and girilen_sifre == sifre:
        print("ÖĞRENCİ NOT OTOMASYON SİSTEMİNE HOŞGELDİNİZ")
    else:
        print("KULLANICI ADI YANLIŞ LÜTFEN TEKRAR DENEYİNİZ ")
        exit()

    subjects = ["Matematik", "İşletme", "Algoritma", "İşlem Tabloları", "Pazarlama"]
    grades = []

    for subject in subjects:
        vize = int(input(f"{subject} DERSİ VİZE NOTU GİRİNİZ: "))
        final = int(input(f"{subject} DERSİ FİNAL NOTU GİRİNİZ: "))
        ortalama = calculate_subject_average(vize, final)
        not_durumu = get_grade(ortalama)
        grades.append((subject, ortalama, not_durumu))
        print(f"{subject} DERSİNİN ORTALAMASI = {ortalama} - {not_durumu}")

    print("\nGENEL ORTALAMA")
    gort = sum(grade[1] for grade in grades) / len(grades)

    if gort >= 49.5:
        print(f"{gort} ORTALAMA İLE ÖĞRENCİ BAŞARILI")
    else:
        print(f"{gort} ORTALAMA İLE ÖĞRENCİ BAŞARISIZ")

if __name__ == "__main__":
    main()