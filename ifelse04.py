# Bank hisobini tekshirish

withdraw = float(input("Yechmoqchi bo'lgan summani kiriting: "))
balance = 5000

if withdraw < balance:
    print(f"Pul yechildi. Qolgan summa: {balance - withdraw}")

else:
    print(f"Mablag' yetarli emas. Sizning balansingiz: {balance} so'm")