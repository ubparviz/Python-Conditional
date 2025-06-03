# Kun davomidagi vaqt

time = int(input("Soat Nechchi?: "))

if time >= 5 and time <= 11:
    print("Ertalab")

elif time >= 12 and time <= 17:
    print("Kunduzi")

elif time >= 18 and time <= 21:
    print("Kechqurun")

elif time >= 22 or time <= 4:
    print("Tun")

elif time > 23 or time < 0:
    print("Vaqtni xato yozdiz. (0-23) oralig'ida bo'lsin")