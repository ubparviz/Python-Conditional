# Fayl mavjudligini tekshirish

import os

file_name = input("Fayl nomini kiriting: ")

if os.path.exists(file_name):
    print("Fayl bor")

else:
    print("Bunaqa fayl yoq")