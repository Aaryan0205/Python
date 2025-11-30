# # # a=-100
# # # b=450
# # # c=0
# # # if a>0 or b>0:
# # #  print("true")
# # # else:
# # #  print("false")
# # # if a==0 and b==0:
# # #  print("true")
# # # else:
# # #  print("false")
# # a="Aaryan"
# # b="Bhaumik"
# # if a!=b:
# #  print("a and b are different")
# # else:
# #  print("they are same")
# a=4 
# b=5
# if (a==1)!=(b==5):
#     print("hello")
#     print(b)
Weight=float(input("enter your weight"))
Height=float(input("enter your height"))
BMI=Weight/(Height/100)**2
print(BMI)
if BMI<=18:
    print("under weight")
elif BMI<=24:
    print("healthy")
elif BMI<=29:
    print("over weight")
elif BMI<=34:
    print("obise")
else:
    print("sevierly obise")
