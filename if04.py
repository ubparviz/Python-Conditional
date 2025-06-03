# Yoshini so'rang va chegirmani qo'llang:

template = "Yoshiz {age} yoshda ekan. Chipta narxi siz uchun {chipta} ming so'm"

age = int(input("Yoshingizni kiriting: "))
ticket = 100

if age < 7:
    ticket *= 0.5
    print(template.format(age=age, chipta=ticket))

if age >= 7 and age <= 17:
    ticket *= 0.8
    print(template.format(age=age, chipta=ticket))
    
if age > 60:
    ticket *= 0.7
    print(template.format(age=age, chipta=ticket))