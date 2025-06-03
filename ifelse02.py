# Parol tekshiruvi

password = input("Parol kiriting: ")

if len(password) >= 8 and not password.isalnum() and not password.isdigit():
    print("Parol qabul qilindi.")

else:
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak.")