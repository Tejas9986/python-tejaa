# print("Aum KaalBhairavay Naamh")


# list = [1, 2, 3,0, 3, 0, 3, 0]

# for item in list:
#     if item == 0:
#         list.remove(item)
#         list.append(item)

# print(list)

# num1 = int(input("Enter Num1: "))
# num2 = int(input("Enter Num2: "))

# if (num1 * num2 >1000):
#     print("The product of num1 and num2 is: ", num1*num2)

# else:
#     print("The sum of num1 and num2 is: ", num1+num2)

def product(num1, num2):
    if num1*num2 > 1000:
        return num1*num2
    
    return num1 + num2


print(product(2, 3))
print(product(88, 98))