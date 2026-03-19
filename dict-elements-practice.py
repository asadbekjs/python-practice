# Amaliyot
# 1.
python_dict = {
    "integer": "butun son",
    "float": "o'nlik son",
    "string": "matn",
    "boolean": "mantiqiy qiymat",
    "list": "ro'yxat",
    "tuple": "o'zgarmas ro'yxat",
    "input": "foydalanuvchi kiritgan ma'lumot",
    "print": "ekran chiqarish funksiyasi",
    "if": "shart operatori",
    "for": "tsikl operatori",
    "while": "tsikl operatori"
}
for key, value in sorted(python_dict.items()):
    print(f"{key.title()} - {value}")
# 2. 
davlatlar = {
    "o'zbekiston": "toshkent",      
    "rossiya": "moskva",
    "aqsh": "vashington",       
    "italiya": "rim",
    "fransiya": "parij",
    "germaniya": "berlin",
    "ispaniya": "madrid",
    "qozog'iston": "ostona",
    "qirgiston": "bishkek",
    "turkmaniston": "ashgabat"
}
print("Davlatlar:")
for davlat in sorted(davlatlar.keys()):
    print(davlat.title())
print("\nPoytaxtlar:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
# 3.
# 1-usul:
kalit = input("Davlat nomini kiriting: ").strip().lower()
if kalit in davlatlar:
    print(f"{kalit.title()}ning poytaxti: {davlatlar[kalit].title()}")
else:
    print("Bizda bunday ma'lumot yo'q")

# 2-usul:
if davlatlar.get(kalit) == None:
    print("Bizda bunday ma'lumot yo'q")
else:
    print(f"{kalit.title()}ning poytaxti: {davlatlar.get(kalit).title()}")