"""

Sprint_1a task

1) 123 rəqəmini string/character ə çevirin və tipini yoxlayın.
2) 19.99 dəyərini tam ədədə çevirin və nəticəni çap edin.
3) "500" dəyərini numericə çevirin və 2-yə bölüb nəticəni çap edin.
4) a = 8 və b = 12 yaradın. a < b və a == b şərtlərini yoxlayın, nəticələri çap edin.
5) x = 5, y = 10, z = 15 yaradın. (x < y) and (y < z) şərtini yoxlayın və nəticəni çap edin.
6) 25-i 4-ə bölün. Tam bölmə, qalıq və adi bölmə nəticələrini çap edin.
7) 3-ü 4-cü dərəcəyə qaldırın və nəticəni çap edin.
8) qiymet = 75.5 yaradın. Onu tam ədədə çevirin və tipini yoxlayın.
9) n = 20 yaradın. (n > 10) or (n < 5) və (n > 15) and (n < 25) şərtlərini yoxlayın, nəticələri çap edin.
10) "42.8" dəyərini əvvəl float-a, sonra tam ədədə çevirin və hər addımda tipi yoxlayın."""


# 1) 123 rəqəmini string/character-a çevirin və tipini yoxlayın.
num = 123
num_str = str(num)
print("1:", num_str, type(num_str))

# 2) 19.99 dəyərini tam ədədə çevirin və nəticəni çap edin.
float_val = 19.99
int_val = int(float_val)
print("2:", int_val)

# 3) "500" dəyərini numeric-ə çevirin və 2-yə bölüb nəticəni çap edin.
str_val = "500"
numeric_val = int(str_val)
result = numeric_val / 2
print("3:", result)

# 4) a = 8 və b = 12 yaradın. a < b və a == b şərtlərini yoxlayın, nəticələri çap edin.
a = 8
b = 12
print("4: a < b:", a < b)
print("4: a == b:", a == b)

# 5) x = 5, y = 10, z = 15 yaradın. (x < y) and (y < z) şərtini yoxlayın və nəticəni çap edin.
x = 5
y = 10
z = 15
print("5:", (x < y) and (y < z))

# 6) 25-i 4-ə bölün. Tam bölmə, qalıq və adi bölmə nəticələrini çap edin.
bolunen = 25
bolen = 4
tam_bolme = bolunen // bolen
qaliq = bolunen % bolen
adi_bolme = bolunen / bolen
print("6: Tam bölmə:", tam_bolme)
print("6: Qalıq:", qaliq)
print("6: Adi bölmə:", adi_bolme)

# 7) 3-ü 4-cü dərəcəyə qaldırın və nəticəni çap edin.
power_result = 3 ** 4
print("7:", power_result)

# 8) qiymet = 75.5 yaradın. Onu tam ədədə çevirin və tipini yoxlayın.
qiymet = 75.5
qiymet_int = int(qiymet)
print("8:", qiymet_int, type(qiymet_int))

# 9) n = 20 yaradın. (n > 10) or (n < 5) və (n > 15) and (n < 25) şərtlərini yoxlayın, nəticələri çap edin.
n = 20
print("9: (n > 10) or (n < 5):", (n > 10) or (n < 5))
print("9: (n > 15) and (n < 25):", (n > 15) and (n < 25))

# 10) "42.8" dəyərini əvvəl float-a, sonra tam ədədə çevirin və hər addımda tipi yoxlayın.
val_str = "42.8"
val_float = float(val_str)
print("10: Float:", val_float, type(val_float))
val_int = int(val_float)
print("10: Int:", val_int, type(val_int))
