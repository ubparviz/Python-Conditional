# BMI hisoblash va tasnif

import sys



height = float(input("Bo'yingizni kiriting (metrda): "))

if height <= 0:
    print("Vazn va bo'y musbat bo'lishi kerak")
    sys.exit()

elif height < 0.5 or height > 3:
    print("Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak")
    sys.exit()


weight = float(input("Vazningizni kiriting (kgda): "))

if weight <= 0:
    print("Vazn va bo'y musbat bo'lishi kerak")
    sys.exit()

elif weight < 1 or weight > 500:
    print("Vazn 1-500 kg oralig'ida bo'lishi kerak")
    sys.exit()




BMI = weight / pow(height, 2)

if BMI < 16:
    print("Og'ir ozg'inlik!")

elif BMI >= 16 and BMI <= 16.9:
    print("Jiddiy ozg'inlik!")

elif BMI >= 17 and BMI <= 18.4:
    print("Yengil ozg'inlik!")

elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal sog'lom vazn!")

elif BMI >= 25 and BMI <= 29.9:
    print("Ortiqcha vazn!")

elif BMI >= 30 and BMI <= 34.9:
    print("I darajali semizlik!")

elif BMI >= 35 and BMI <= 39:
    print("II darajali semizlik!")

elif BMI >= 40:
    print("III darajali (juda og'ir) semizlik!")



print(BMI)