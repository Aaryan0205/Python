# Attendence=90
# if Attendence>75:
#     if Attendence>90:
#         print("Bonus Marks")
#     elif Attendence==90:
#         print("Eligable")
# else:
#     print("Not Eligable")

# a=93
# if a<50:
#     print(a*2.6)
# elif a<100:
#     print(a*3.2)
# else:
#     print(a*5.2)

print("select your ride")
print("1. Car")
print("2. Bike") 
Choice=int(input("enter your choice"))
if Choice==1:
    print("car") 
    print("1.Sedan")
    print("2.SUV")
    Choice1=int(input("Enter your choice"))
    if Choice1==1:
        print("Sedan")
    else:
        print("SUV")
else:
    
    print("Bike")
    print("1.Scooty")
    print("2.Sport bike")
    Choice2=int(input("Enter your choice"))
    if Choice2==1:
        print("Scooty")
    else:
        print("Sport bike")
