# Baholash tizimi

ball = int(input("Balingizni kiriting: "))

if ball >= 90 and ball <= 100:
    print("A'lo")

elif ball >= 80 and ball <= 89:
    print("Yaxshi")

elif ball >= 70 and ball <= 79:
    print("Qoniqarli")

elif ball >= 60 and ball <= 69:
    print("Qoniqarsiz")

elif ball >= 0 and ball <= 59:
    print("Rad")

elif ball > 100 or ball < 0:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")