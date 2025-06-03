# Son: 2,3,5 ga bo'linishini hisoblang

template = "{a} soni {b} ga bo'linadi!"

number = int(input("Son kiriting: "))

if number % 2 == 0:
    print(template.format(a=number, b=2))

if number % 3 == 0:
    print(template.format(a=number, b=3))

if number % 5 == 0:
    print(template.format(a=number, b=5))