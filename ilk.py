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



# 1
s = "Programming"
print(len(s))       # Uzunluğu
print(s[0])         # İlk simvolu

# 2
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

# 3
text = "Python"
print(text[-1])     # Son simvol

# 4
s = "Artificial"
print(s.replace("Art", ""))  # "Art" hissəsini çıxarır

# 5
word = "Code"
print(word[::-1])   # Tərsinə çevrilmiş versiya

# 6
s = "abcdefgh"
print(s[::2])       # Hər ikinci simvol

# 7
text = "data"
print(text.upper(), text.lower())

# 8
s = "Python-R-Java"
print(s.split("-"))

# 9
ad = "Ayxan"
yaş = 25
print(f"{ad} {yaş} yaşındadır")

# 10
s = "salam-dunya"
print(s.replace("-", " "))


import pandas as pd

# 1
s1 = pd.Series([10, 20, 30, 40])

# 2
s1.index = ['w', 'x', 'y', 'z']

# 3
s2 = pd.Series({'p': 5, 'q': 10, 'r': 15})

# 4
print(s2['q'])

# 5
print(s1[s1 > 25])

# 6
print(s1[s1 > 20] / 10)

# 7
df1 = pd.DataFrame([[1, 2], [3, 4]])

# 8
df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']

# 9
df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# 10
print(df2[df2['A'] > 1])

# 1
rəqəmlər = [5, 10, 15, 20]

# 2
print(len(rəqəmlər))

# 3
rəqəmlər.append(25)

# 4
rəqəmlər.insert(2, 12)

# 5
birləşmiş = [1, 2, 3] + [4, 5, 6]

# 6
print(rəqəmlər[2:4])

# 7
rəqəmlər[0] = 50

# 8
print(19 in rəqəmlər)

# 9
lst = ["a", "b", "a", "c"]
print(lst.count("a"))

# 10
lst2 = ["x", "y", "x", "z"]
lst2 = [el for el in lst2 if el != "x"]

# 11
print(sorted([7, 2, 9, 1], reverse=True))

# 12
print([x for x in rəqəmlər if x > 10])
