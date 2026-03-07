# ismlar = ['Abror', 'Mahmud', 'Jamol']
# print(f"Salom {ismlar[0]}, bugun choyxona bormi?\n{ismlar[1]} choyxonaga boramizmi?")

# sonlar = [12, 15, 0, 89, -15.75, 0, 158.89]
# print(sonlar[3] / sonlar[1]) # 89 / 15 
# 0 => -8
# sonlar[2] = -8
# print(sonlar)

# historical_people = ['Amir Temur', 'Alisher Navoiy', 'Julia Sezar', "Al-Xorazmiy"]
# modern_people = ['Bill Gates', 'Ilon Musk', 'Pavel Durov', 'Steve Jobs']
# print(f"""Men tarixiy shaxslardan {historical_people[3]} bilan,
# zamonaviy shaxslardan esa {modern_people[3]} bilan,
# suhbat qilishni istar edim""")

friends = ['mahliyo', 'nodira', 'dilmira', 'lobar', 'zebo', 'asal']
# friends.append("yulduz")
# friends.insert(0, 'maftuna')
# print(friends)
# element = friends.pop(1)
# print(friends)
# print(element)

# list.sort()
# friends.sort() # alifbo(english) bo'yicha tartiblaydi
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# sorted() function
# sorted_list = sorted(friends, reverse=True)
# print(friends)
# print(sorted_list)

# nums = [12, -5, 0, 8.75, 99, 10]
# nums.sort() # o'shish tartibi
# print(nums)
# print(sorted(nums, reverse=True)) # kamayish tartibi

# list.reverse()
# nums.reverse()
# print(nums)

# list() function
users = ['john', 'alisa', 'aziz', 'alex']
cars = list(('bmw', 'audi', 'porsche', 'ford'))
print(cars)
# range() - ma'lum bir oraliqdagi sonlarni shakllantirish uchun ishlatilanadi
# range(start, stop, step?)
# step_default_value = 1
# range(1, 10) # 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = list(range(2, 20, 2))
print(even_nums)
odd_nums = list(range(1, 20, 2))
print(odd_nums)

# SONLI RO'YXAT USTIDA SODDA AMALLAR
narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# min() / max() / sum()
eng_arzoni = min(narxlar)
eng_qimmati = max(narxlar)
yigindi = sum(narxlar)
print(eng_arzoni, eng_qimmati, yigindi)

# Ro'yxatni kesib olish
students = ['Akmal', 'Jasur', 'Asal', 'Kumush', 'Maftuna', 'Elbek']
# new_list = list[start_index : end_index]
# 1-case
students1 = students[2 : 5]
students2 = students[0 : 2]
print(students1, students2)
# 2-case
students3 = students[1 : ] # start_index dan boshlab oxirigicha kesib oladi
print(students3)
# 3-case
students4 = students[ : 4] # ro'yxat boshidan end_index gacha kesadi
print(students4)

# 0 dan boshlab indekslanadi
# manfiy index -1 dan boshlanadi (-1, -2, -3)
print(students[-1])
print(students[-2])
print(students[-5])
print(students[-4 : -2])

# RO'YXATDAN NUSXA(COPY) OLISH
# 1. Shallow(sayoz) copy
sonlar = [1, 5, -5, 12]
# sonlar2 = sonlar
# sonlar2.append(77)
# sonlar.insert(2, -8)
# print(sonlar2)
# print(sonlar)
# 2. Deep(chuqur) copy
sonlar3 = sonlar[:]
sonlar3.append(8)
print(sonlar3)
print(sonlar)

# deep copy using copy library
import copy
original_list = [1, 2, [3, 4], 5]
deep_copy = copy.deepcopy(original_list)

deep_copy[2].append(99)
print(deep_copy)
print(original_list)

# Tuple - o'zgarmas ro'yxat
toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])
# toys[1] = 'dragon'
# print(toys) # error

toys = list(toys)
toys[1] = "dragon"
toys.remove("dino")
toys.append("mcqueen")
toys = tuple(toys)
print(toys)

# 
sonlar = list(range(120, 1200, 2))
# boshidan 20 ta element
print(sonlar[ : 20])
# oxiridan 20 ta element
print(sonlar[-20 : ])
# o'rtasidan 20 ta element
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(sonlar)
start_index = length // 2 - 10
end_index = length // 2 + 10
print(sonlar[start_index : end_index])