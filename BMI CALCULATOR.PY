print(" BMI CALCULATOR ")
print(" ************** ")
print("\n")
height=float(input("ENTER YOUR HEIGHT IN CENTIMETER(cm):"))
print("\n")
weight=float(input("ENTER YOUR WEIGHT IN KILOGRAMS(kg):"))
height=height/100
BMI=weight/(height)**2
print("\n")
print("YOUR BMI IS:",BMI)
print("\n")
if BMI<=16:
    print("SEVERE THINNESS")
elif BMI<=17.5:
    print("MODERATE THINNESS")
elif BMI<=18.5:
    print("MILD THINNESS")
elif BMI<=25:
    print("NORMAL WEIGHT")
elif BMI<=30:
    print("OVERWEIGHT")
elif BMI<=35:
    print("OBESE CLASS 1")
elif BMI<=40:
    print("OBESE CLASS 2")
elif BMI>40:
    print("OBESE CLASS 3")
