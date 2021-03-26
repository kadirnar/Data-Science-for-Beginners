        #Numpy Temelleri

#%% Temel İşlemler

import numpy as np

a = [1,2,3]
b = np.array(a) # numpy dizisi oluşturur.
c = np.arange(1,10) # 1'den 10 kadar sıralama yapar
d = np.zeros((3,3)) # x tane 0'lı matris oluşturur.
e = np.linspace(0,20,10) # 0'dan 20'ye kadar 10 tane rastgele matris oluşturur.
f = np.random.randint(0,1,10) # 0'dan 1'e kadar 10 tane rastgele dizi oluşturur.

#%% Numpy Metodları

dizi = np.random.randint(0,10,6)
dizim = dizi.reshape(2,3)
dizim.shape # dizinin satır ve sütür bilgisini veriyor.
dizim.ndim # boyut bilgisi

#%% İndex İşlemleri

#Gerek olmadığı için ders işlenmemiştir.



#%%        # Pandas Temelleri

#Seriler

import pandas as pd

sozluk = {"Serhat:":22, "Kadir":21, "Batu":21}
a = pd.Series(sozluk)

T = pd.Series(["T","S","İ"],["Akıncı","Tb2","Baykar Mini İha"]) 
İ = pd.Series(["İ","İ","H"],["Akıncı","Tb2","Baykar Mini İha"])
H = pd.Series(["H","H","A"],["Akıncı","Tb2","Baykar Mini İha"]) 
A = pd.Series(["A","A",""],["Akıncı","Tb2","Baykar Mini İha"])

baykar = T+İ+H+A


#%%  Dataframe

data = np.random.randn(3,3)

dataFrame = pd.DataFrame(data)

dframe = pd.DataFrame(data,index = ["Akıncı","Tb2","Baykar Mini İha"], columns = ["1.Özellik","2.Özellik","3.Özellik"])

# Daha sonra öğrenmek üzerine buralar geçilmiştir.

#%% TensorFlow Temelleri

 




#%%





#%%




#%%







#%%
