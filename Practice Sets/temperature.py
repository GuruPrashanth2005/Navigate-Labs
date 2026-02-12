# marks=int(input("Enter marks: "))
# if marks<0 or marks>100:
#     print("Invalid marks")
# elif marks>=90:
#     print("Excellent")
# elif marks>=75:
#     print("Good") 
# elif marks>=50:
#     print("Averaege")
# else:
#     print("Need Improvement")



# temperature=int(input("Enter temperature: "))
# if temperature<0:
#     print("Invalid Temperature")
# elif temperature==38:
#     print("Fever Detected")
# else:
#     print("normal")



# units=int(input("Enter units:"))
# bill=0
# if units<=100:
#     bill=units*2
# elif units<=200:
#     bill=100*2+(units-100)*3
# else:
#     bill=100*2+100*3+(units-200)*5
# print("Bill amount is:",bill)



# salary=int(input("Enter salary: "))
# tax=0
# if salary<250000:
#     tax=0
# elif salary>=250000 and salary<500000:
#     tax=0.05*salary
# elif salary==500000:
#     tax=0.1*salary
# print("Tax amount is:",tax)
# print("salary after tax:",salary-tax)



# price=int(input("Enter price: "))
# if price>=200:
#     discount=0.2*price
# elif price>=100:
#     discount=0.1*price
# print("Discount amount is:",discount)
# print("Price after discount:",price-discount)   



# weight=float(input("Enter weight: "))
# height=float(input("Enter height in m: "))
# bmi=weight/(height*height)
# if bmi<18.5:
#     print("Underweight")
# elif bmi<24.9:
#     print("Normal weight")
# elif bmi==25:
#     print("Overweight")


# units=int(input("Enter units: "))
# if units<=100:
#     bill=0
# elif units<=300:
#     bill=(units-100)*2
#     if bill>200:
#         bill+=50
# elif units>300:
#     bill=200*2+(units-300)*5
#     bill+=100
# print("Total bill amount is:",bill)


# amount=int(input("Enter amount: "))
# membership=input("Enter membership type (Yes/No): ").lower()
# discount=0
# if amount<0:
#     print("Invalid amount")
# elif amount>=3000:
#     if membership=="yes":
#         discount=0.30*amount
#     else:
#         discount=0.20*amount
# elif amount>=1000:
#     if membership=="yes":
#         discount=0.15*amount
#     else:
#         discount=0.10*amount
# else:
#     discount=0
# print("Discount amount is:",discount)
# print("Amount after discount:",amount-discount)

# n=int(input("Enter a number: "))
# total=0
# for i in range(1,n+1):
#     total+=i
# print("sum is:",total)

# n=int(input("Enter a number: "))
# count=0
# for i in range(1,n+1):
#     if i%2==0:
#         count+=1
# print("Count:",count)


# n=int(input("Enter a number: "))
# for i in range(0,n+1):
#     for j in range(0,i):
#         print(i,end="")
#     print()


# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()


# n=int(input("Enter a number: "))
# for i in range(0,n):
#     for j in range(i+1):
#         print(j+1 ,end="")
#     print()

