# Funksiya Tapşırıqları

def salam():
    print("Salam, Dünya!")

def kub_hesabla(n):
    return n ** 3

def birlesdir(soz1, soz2):
    return soz1 + " " + soz2

def cap_et(lst):
    for item in lst:
        print(item)

def toplam(*args):
    return sum(args)

def ortalama(*args):
    if len(args) == 0:
        return "Rəqəm yoxdur"
    return sum(args) / len(args)

def adlar_rəqəmlər(**kwargs):
    for ad, reqem in kwargs.items():
        print(f"ad: {ad}, rəqəm: {reqem}")

def tip_yoxla(dəyər):
    if isinstance(dəyər, str):
        print("mətn")
    elif isinstance(dəyər, (int, float)):
        print("rəqəm")
    else:
        print("başqa")

def yas_kateqoriya():
    yas = int(input("Yaşınızı daxil edin: "))
    if yas < 18:
        print("Gənc")
    else:
        print("Yetkin")

def soz_uzunluq():
    soz = input("Bir söz daxil edin: ")
    print(len(soz))



# 1) x dəyişəni
x = 5  # nümunə üçün
if x > 0:
    print("müsbət")
elif x < 0:
    print("mənfi")
else:
    print("sıfır")

n = 7
if n % 2 == 0:
    print("cüt")
else:
    print("tək")

a, b, c = 5, 8, 3
print(max(a, b, c))

day = 3
days = {
    1: "Bazar ertəsi",
    2: "Çərşənbə axşamı",
    3: "Çərşənbə",
    4: "Cümə axşamı",
    5: "Cümə",
    6: "Şənbə",
    7: "Bazar"
}
print(days.get(day, "Yanlış gün"))

temp = 15
if temp < 0:
    print("soyuq")
elif 0 <= temp <= 20:
    print("normal")
else:
    print("isti")

# 6) password string
password = "12345678"
if len(password) < 8:
    print("qısa")
elif 8 <= len(password) <= 12:
    print("orta")
else:
    print("uzun")

x = 15
if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

for i in range(0, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()

s = "Bağda ərik var idi …"
for ch in s:
    print(ch)

for i in range(1, 11):
    if i == 3:
        continue
    print(i)

i = 1
while True:
    if i % 5 == 0:
        print(i)
        break
    i += 1

# 12) 5-i tap və indeksini çap et
numbers = [1, 3, 5, 7, 9]
for index, value in enumerate(numbers):
    if value == 5:
        print(index)
        break
