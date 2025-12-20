# a=int(input("Enter the number"))
# sum=0
# i=1
# while i<=a:
#     sum=sum+i
#     i=i+1
#     print(sum)

# i=0
# while i<=0:
#     print("hello")

a=int(input("enter the number"))
sum=0
Temp=a
while Temp>0:
    d=Temp%10
    sum+=d**3
    Temp//=10
if a==sum:
    print("Armstrong number") 
else:
    print("Not an Armstrong number")  
