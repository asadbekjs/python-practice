# 115
# numbers = [85, 15, 57, 68, 18, 67, 7, 45, 69, 21, 1, 5, 98, 34]
# m = int(input("m sonini kiriting: "))
# s = 0
# for number in numbers: 
#     if number < m:
#         s += number ** 2

# print(s)

# 122
# sonlar = [44, 59, -75, 73]
# s = 0
# p = 0
# for son in sonlar:
#     p += son ** 2
#     s += son

# ortacha_qiymat = s / len(sonlar) 
# print(p)
# print(ortacha_qiymat)

# 126
# plan: 1. o'rtacha qiymat 2. o'r_qiy logni topish
# 3. manfiy elementlarini topish 4. manfiy elementlarni o'r_qiy logiga almashtirish
# import math
# nums = [7, 24, -5, 23, 99, -3, 24, 51] 
# # nums[2] = 12
# s = 0
# for num in nums:
#     s += num
# length = len(nums)
# average_value = s / length
# log_value = math.log(average_value)

# for index in range(length):
#     if nums[index] < 0:
#         nums[index] = log_value

# print(nums)

# 127 - HOMEWORK 
# 123 
# numbers = [3, 17, -59]
# plan: 1. juft o'rinli elementlar 2. juft o'rinlar elementlar yigindisi
# 3. toq qiymatli qiymatli elementlar 4. toq qiy el j_o'_e_y ga bo'lish
# s = 0
# for index in range(len(numbers)):
#     if (index + 1) % 2 == 0:
#         s += numbers[index] 

# for number in numbers:
#     if number % 2 == 1:
#         print(number / s, " ")
#     else: 
#         print(number, " ")

# 104
# plan:
# 1. min qiymatni topish
# 2. oxirgi qiymat => list[-1] / list[len(list) - 1] 
# 3. almashtirish => index orqali almashtiramiz
# numbers = [74, 0, 1, 33]
# min_value = min(numbers)
# last_element = numbers[-1]
# # print(numbers.index(1)) // 2
# # numbers[3] = 75
# min_index = numbers.index(min_value)
# numbers[min_index], numbers[-1] = last_element, min_value
# print(*numbers)

# a = 5
# b = 2
# result: a = 2; b = 5
# 1-usul:
# a, b = b, a

# 2 - usul:
# c - temporary variable
# c = a
# a = b
# b = c

# 3-usul
# [a, b] = [b, a]
# print(a, b)
numbers = [29, 50, -14, 4, 27, -56]
k = int(input())
max_value = max(numbers)
k_index = k - 1
max_index = numbers.index(max_value)
numbers[max_index] = numbers[k-1]
numbers[k-1] = max_value
print(*numbers)