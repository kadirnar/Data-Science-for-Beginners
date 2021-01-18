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

x = []
y = 0
while y<10:
    y = y+1
    x.append(y) # x dizinine 0,1..10 kadar sayıları ekledi.
    
#%% range

a = list(range(1,20,2))
b = []
for i in a:
    islem = (i*2)-2
    b.append(islem)
    
#%% enumerate
a = list(range(1,20,2))

for x,y in enumerate(a):
    print(x,y)

# range fonksiyonun 1. ve 2. elemanları 
#%% random

import random
a = random.randint(1,100)
b = list(range(10))
random.shuffle(b) #b listesini karıştır.


#%% zıp

a = ["a","b","c"]
b = [1,2,3]
c = ["q","w","e"]
d = list(zip(a,b,c))

#%%

a = [1,2,3,4]
b =[i for i in a] # a dizinindeki elemanları b'ye yaz.

x = [y*2 for y in list(range(10))]

#%% return

a = int(input("sayi gir:"))
b = int(input("sayi gir:"))
def hesapla(a,b):
    print("kadri")
a = hesapla(a,b) #fonksiyonu bi değişkene atmamız için return yazılmalı.

#%% args & kwargs

def hesapla(*args):
    return args

a = hesapla(10,30,20)

def hesap(**kwargs):
    return kwargs
b = hesap(muz=100, elma=200, armut=300)

#%% map

x = [1,2,3]
def abc(y):
    return y*2

k = list(map(abc,x))

#%% lambda 

a = lambda b:b**2 #tek satırda fonksiyon yazdırıyor.
print(a(5))

#%%




#%% global ve local değişkenler

x = 1

def fonk():
    global x #def dışında da x değerimiz 2'ye eşittir.
    x = 2
    print(x)
fonk()    

#%% Hesap Makinası

def HesapMakinesi():
    
    while True:
        try:
        
            sayi1 = int(input("1.Sayi: "))
            sayi2 = int(input("2.Sayi: "))
            islem = input("İşlem türünü seçiniz: ")  
            if islem == "+":
            
                toplama = sayi1+sayi2
                print(toplama)
                
            elif islem == "-":
            
                cıkarma = sayi1-sayi2
                print(cıkarma)
        
            elif islem == "*":
                
                carpma = sayi1*sayi2
                print(carpma)
        
            elif islem == "/":
                
                bölme =sayi1/sayi2
                print(bölme)
        except:
            print("Sayıları düzgün giriniz.")

HesapMakinesi()
#%%                        SINIFLAR

#Basit bir class yapısı oluşturuyoruz.

class Plane():
    def __init__(self):
        print("uçak")

uavs = Plane()
#%%

class UavTeam():
    def __init__(self,teamMembers,teamDuties):
        self.members = teamMembers
        self.duties = teamDuties

teams  = UavTeam("kadir","Deep Learning Researcher")

print(teams.duties)
#%%

class Uav():
    def __init__(self):
        print("Uav Takımı")
    
    def sabit(self):
        print("Sabit Kanat")
        
    def döner(self):
        print("Döner Kanat")
        
class Teknofest(Uav): 
    def __init__(self):
        Uav.__init__(self)
        print("Teknofest Ekipleri")
        
    
    def UavTakımları(self):
        print("Tübitak Ekipleri")

SelcukBayraktar = Teknofest() # Tüm teknofest yarışmalaarını kapsar
Tübitak = Uav() # Sadece Tübitak yarışmalarını kapsar.
