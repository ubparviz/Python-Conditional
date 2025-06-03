# Foydalanuvchidan haroratni (°C) so'rang va maslahat bering:

harorat = int(input("Haroratni kiritng: "))

if harorat < 0:
    print("Juda Sovuq, Issqi kiyim kiying.")

if harorat >= 0 and harorat <= 14:
     print("Sovuq, Kurtka kiying.")
     
if harorat >= 15:
     print("Ob-havo yaxshi.")