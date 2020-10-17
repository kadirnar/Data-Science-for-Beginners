                     # Python Temelleri

#%% Matematiksel İşlemler

a = 2*2 #çarpma
b = 2/2 #bölme
c = 2-2 #çıkarma
d = 2+2 #toplama
e = 2//2 #çarpanı bulma
f = 2%2 #kalan bulma
g = 2**2 #üssünü alma

#%% İndex İşlemleri

a = "kadir nar"
a[1:5:2] # çıktı olarak "ai" yazdıracaktır.

#%% Listeler

a = [1,2,3,4,5]

a[2] = 4 # 2.indexdeki elemanı değiştirme
a.append(5) #liste sonuna ekleme
a.pop(4) #index sırasına göre eleman silme
a.insert(2, 45) # index,eklenecek eleman
a.sort(reverse=True) # Büyükten küçüğe sıralama

#%% Sözlükler

a = {"elma":1,"armut":2,"nar":3}
a.keys() #1.eleman
a.values() #2.eleman

#%% Setler

a = {1,2,3}
type(a)
# setlerde 1 değerden sadece 1 tane bulunabilir.

#%% Tuple

a = (1,2,3)
# Tuple veri tipleri asla değiştirilemez.

#%% Bool

a = 5
b = 4

a = [1,2,3,4,5]
b = sum(a) #toplama
ortalama = b/len(a) #len():karakter sayısını bulmak için.
b<ortalama #False döndürecektir.
#--------------------------------------------------

3<4 and 2<1 #2 koşulu da sağlamalı.
3<4 or 2<1 # tek koşul kafidir.

#%% if Kontrolleri

x = 10
y = 20

if x<y:
    print("y, x'den büyüktür.")
elif y<x:
    print("y, x'den büyüktür.")
else:
    print("y, x'e eşittir.")

"a" in "kadir" # kadir kelimesinde a harfi var?True

a = [1,2,4,5]
if 3 in a:
    print("a dizininde 3 sayısı vardır.")
else:
    print("a dizininde 3 sayısı yoktur.")

#%% For Döngüsü

numara = [1,2,3,4,5]

for sayi in numara:
    kalan = sayi%2
    if kalan%2 == 0:
        print("Sayi:{} Kalan:{} ".format(sayi,kalan))
    else:
        
        print("Sayi:{} Kalan:{} ".format(sayi,kalan))

#----------------------------------------------------

a = [[1,2,3],[4,5,6],[7,8,9]]

for x,y,z in a:
    print(x,y,z)

#%% Contiune-Break

numara = [1,2,4,5]

for i in numara:
    if i == 3:
        break # 3 sayısına kadar devam et
    print(i)

for i in numara:
    if i == 3:
        continue # sadece 3 sayısını dahil etme.
    print(i)

#%% While Döngüsü












