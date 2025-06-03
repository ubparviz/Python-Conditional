# Transport tanlash

distance = float(input("Masofani yozing (km): "))

if distance > 0 and distance <= 1:
    print("Piyoda yuring!")

elif distance > 1 and distance <= 5:
    print("Velosiped yoki elektr skuter")

elif distance > 5 and distance < 50:
    print("Avtobus yoki mashina")

elif distance >= 50:
    print("Poyezd yoki samolyot")

if distance < 0:
    print("Masofa manfiy bo'la olmaydi!")