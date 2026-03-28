# Amaliyot
# 1.
# def tugilgan_yilni_topish(ism,yosh):
#     yil = 2026 - yosh
#     print(f"{ism} {yil}-yilda tug'ilgan")

# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# tugilgan_yilni_topish(ism, yosh)

# 2.
# def kvadrat_kub_hisobla(son):
#     kvadrat = son ** 2
#     kub = son ** 3
#     print(f"{son}ning kvadrati: {kvadrat}, kubi: {kub}")

# son = int(input("Sonni kiriting: "))
# kvadrat_kub_hisobla(son)

# # 3.
# son = int(input("Sonni kiriting: "))
# def tekshir_son(son):
#     if son % 2 == 0:
#         print("Bu son juft") 
#     else:
#         print("Bu son toq")

# tekshir_son(son)

# # 4.
# def solishtirish(a, b):
#     if a > b:
#         print(f"{a} katta {b} dan")
#     elif a < b:
#         print(f"{a} kichik {b} dan")
#     else:
#         print(f"{a} va {b} teng")

# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: ")) 
# solishtirish(x, y)

# 5 va 6.
# def daraja_hisobla(asos, daraja=2):
#     natija = asos ** daraja
#     print(f"{asos} ning {daraja} darajasi: {natija}")
    
# x = int(input("Asos sonni kiriting: "))
# y = int(input("Daraja sonni kiriting: "))
# daraja_hisobla(x, y)
# daraja_hisobla(2, 3) # 2 ning 3-darajasi: 8
# daraja_hisobla(5) # daraja 2 ga teng bo'ladi, chunki default qiymat 2 ga teng.

# 7.
def bolinish(son):
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi")

a = int(input("Xoxlagan son kiriting: "))
bolinish(a)