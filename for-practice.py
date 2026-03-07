# ismlar = ["Elbek", "Ibrohim", "G`ulomjon K", "G`ulomjon T", "Rahimboy"]
# for ism in ismlar:
#     print(f"Bugun {ism}. Futbolga kelasizlarmi? ")

# print(f"Code {len(ismlar)} marta takrorlanadi")

# sonlar = list(range(11,100,2))
# for son in sonlar:
#  print(son**3)

# kinolar = []
# for k in range(5):
#  kino = input(f"{k + 1} Sevimli kiongizni kiriting :")
#  kinolar.append(kino)
# print(kinolar)

# number_of_people = int(input("Bugun nechta inson bilan ko'rishdingiz?"))
# ismlar = []

# for son in range(number_of_people):
#   ism = input(f"{son + 1} - ko'rishgan insoniningiz ismini kiriting: ")
#   ismlar.append(ism)

# print(ismlar)

# for son in range(11):
#   print(son)

# s = 0
# numbers = [12, 5, 18, 25, 23]
# for number in numbers:
#   s += number # s = s + number
# print(s)

# # 1 dan 50 gacha toq sonlar yigindisi
# summa = 0
# for son in range(1, 50, 2):
#   summa += son

# print(summa)

# s = 0
# numbers = [12, 5, 18, 25, 23, 88]
# o'rta arifmetik = s / length 
# o'rta geometrik = 
# 1. k = 1250
# 2. length
# 3. k ** (1 / length)
# import math
# l = len(numbers)
# k = 1
# for number in numbers:
#     k *= number
# a = math.pow(k, 1 / l)
# print(a)

# for number in numbers:
#     s += number

# average_value =  s / len(numbers)
# print(average_value)

# 1 dan 20 gacha bo'lgan juft sonlarni o'rta arifmetikini toping
# s = 0
# for number in range(1, 21, 2):
#   s += number
  
# nums = list(range(1, 21, 2))
# average_value = s / len(nums)
# print(average_value)

# n! = 1 * 2 * 3 * ... * (n - 1) * n
# k = 1
# for son in range(1, 20):
#     k *= son # k = k * son

# print(k)

# s = 0
# k = 1
# for number in range(1, 21):
#     if number % 2 == 0:
#         k *= number
#     else:
#         s += number 

# y = k / s
# print(y)
# s = 0
# counter = 0
# numbers = [7, 97, -58, 90]
# for number in numbers:
#     if number % 2 == 0:
#         s += number
#         counter += 1

# print(s / counter)

#
# s = 0
# numbers = [97, 97, -92, 14, 22]
# for number in numbers:
#     if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
#         s += number

# print(s)

s = 0
counter = 0
numbers = [76 , 12, 51, 50, 98]
for number in numbers:
    if number % 2 == 1:
        s += number
        counter += 1

print(s / counter)
