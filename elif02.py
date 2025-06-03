# Kalkulyator, +, -, *, /

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

operators = input("Quydagi amallardan birini kiriting: +, -, /, * : ")

if operators == "+":
    result = a + b
    print(result)

elif operators == "-":
    result = a - b
    print(result)

elif operators == "/":
    if b == 0:
        print("Nolga bo'lish mumkin emas!")
    elif b != 0:
        result = a/b
        print(result)

elif operators == "*":
    result = a*b
    print(result)

elif operators != "*" or "+" or "-" or "/":
    print("Noto'g'ri amal. Faqat +, -, *, / ishlatiladi.")