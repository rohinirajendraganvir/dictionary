fruits = ['mango', 'pear', 'apple','papaya']
price = [90, 78, 110, 60]

fruits_price = zip(fruits, price)


fruits_dict = {}

for key, value in fruits_price:
    if key in fruits_dict:
        
        pass 
    else:
        fruits_dict[key] = value
print(fruits_dict)


# num1=int(input("enter the num1.."))
# num2=int(input("enter the num2.."))
# num3=int(input("enter the num3.."))
# if (num2>num1 or num1>num3 or num3>num1 or num1>num2) :
#     print("num1 is middle")
# elif (num1>num2 or num2>num3 or num3>num2 or num2>num1):
#     print("num2 is middle")
# elif (num1>num3 or num3>num2 or num2>num3 or num3>num1):
#     print("num3 is middle")
# else:
#     print("enter a valid num")


