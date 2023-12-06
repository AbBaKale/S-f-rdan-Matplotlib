# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y_A6zAb3D-Ftvb_v42QsQB7krM25nOiz
"""

#-----------------
# variable (degisken)
#-----------------

var1 = 10 # integer = int
var2 = 15
gun = "pazartesi" # string
var3 = 10.0 # double (float)
var5 = 10
# 5var = 10  # hata verir
var6 = 10
Var7 = 19  # standart convention of python'a gore buyuk harfle baslamasi uygun degil

#-----------------
# string
#-----------------

s = "bugun gunlerden pazartesi"

variable_type = type(s)   # str = string

print(s)

var1 = "ankara"
var2 = "ist"
var3 = var1+var2

var4 = "100"
var5 = "200"
var6 = var4+var5

uzunluk = len(var6)

# var6[3]

# numbers
# int
integer_deneme = -50
# double = float = ondalikli sayi
float_deneme = -30.7


#-----------------
#functionlar
#-----------------
var1 = 20
var2 = 40
def hesap(a,b):
  output=(((a+b*45)/23)*(b/a))
  return output
sonuc= hesap(var1,var2)
print(sonuc)
#sonuc======158.2608695652174
print(hesap(5,15))
#sonuc======88.69565217391305

#-----------------
#Default and Flexible Functions
#-----------------
yari_Cap= int(input("çap gir"))
def cember(r,pi = 3.14):
  cevre=2*pi*r
  return cevre
sonuc_Cevre=cember(yari_Cap,)
print(sonuc_Cevre)

#-----------------
#Lambda Func (amaç daha hızlı func yazma)
#-----------------
sonuc=lambda x: x*x
print(sonuc(4))


#-----------------
#if-else
#-----------------

var=10
var1=20

if var1>var:
  print("var1 büyüktür var dan")
elif var1 == var:
  print("var1 eşittir var ")
else:
  print("var1 küçüktür var dan")

#-------------------------------
list=[1,2,3,4,5,6,7,8,9,0]
value=31
if value in list:
  print("evet {0} değeri listede".format(value))
else:
  print("hayır {0} değeri listede yoktur".format(value))

#-------------------------------
dict={"ali":10 ,"veli":20 ,"ayşe":15 ,"baki":9999}
keys= dict.keys()
if "can" in dict:
  print("listede")
else:
  print("listede değil")

#-----------------
#For Loop
#-----------------

for i in range (1,15):
  print(i)

print("------------------------------------")
#-----------------------
for i in "ali ile veli":
  print(i)
print("------------------------------------")
#-----------------------
for i in "ali ile veli".split():
  print(i)


#-----------------
#while loop
#-----------------

i=0
while i<4:
  print(i)
  i = i+1
print("-----------------------------------")
#-----------------------------------------
liste=[1,2,2,4,5,55,5,77,5,31,77,6,55,87,9,9,]
uzunluk = len(liste)
i=0
count=0
while (i<uzunluk):
  count= count + liste[i]
  i=i+1
  print(count)


#-----------------
#Numpy Basic
#-----------------
#import
import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])# 1 satır 15 sütunluk vectör oluşturduk 1*15
print(array)
print(array.shape) #(15,) 15 sütun 1 satırı yazdırıyor
print("---------------------------------------------")
#reshape farklı şekillendirme
a = array.reshape(3,5)
print(a)
print("shape:",a.shape) #(3, 5) 3 sütun 5 satırlık
print("dimension:",a.ndim) #kaç boyutlu olduğğunu gösterir
print("data type:",a.dtype.name) #int mi str mi tipini gösterir
print("size:",a.size) # büyüklüğünü verir
#--------------------------------------------------------------------
print("---------------------------------------------")
#reshape yapmadan çok boyutlu array oluşturma
array2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])# bunu bir list olarak aldığı için ikinci köşeli parantezi unutma
print(array2)
print("shape:",array2.shape)
print("dimension:",array2.ndim)
print("data type:",array2.dtype.name)
print("size:",array2.size)
#--------------------------------------------------------------------
print("---------------------------------------------")
#sıfırlardan matrix oluşturma ve düzenleme
zeros = np.zeros((4,4))
zeros[0,0]=5
zeros[1,1]=15
zeros[2,2]=25
zeros[3,3]=35
print(zeros)
#zerosun aynısının laciverti birli hali
print("---------------------------------------------")
ones= np.ones((3,4))
print(ones)
#istediğin aralıkta sıra sıra yazdırma
print("---------------------------------------------")
a=np.arange(10,50,5)
print(a) #[10 15 20 25 30 35 40 45]


#------------------------
#Numpy Basic Operations
#------------------------
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b) #[5 7 9]
print(a-b) #[-3 -3 -3]
print(a**2) #[1 4 9]
print(np.sin(a)) #a nın sinüsü [0.84147098 0.90929743 0.14112001]

c = np.array([[1,2,3],[4,5,6]])
d = np.array([[1,2,3],[4,5,6]])
# Element Wise Product
print(c*d) #[[ 1  4  9] [16 25 36]] yani 1*1,2*2,3*3... gibi
# Numpy random sayı oluşturma
e = np.random.random((5,5)) #[[0.33079551 0.80203602 0.88921639 0.75403264 0.67503411]
                            #[0.98856498 0.89455579 0.92063203 0.01087043 0.11265814]
                            #[0.33826436 0.15077962 0.76375961 0.1634163  0.78338111]
                            #[0.31264601 0.8146109  0.46180055 0.15014976 0.56567355]
                            #[0.02081531 0.03028003 0.83605827 0.06469542 0.6452995 ]]

print(e.sum()) #14.52699093794649
print(e.max()) #0.981888696462173
print(e.min()) #0.09163452243891124
print(e.sum(axis=0)) #axis 0 ise column(sütun) sum ile toplar [3.1495896  1.46389878 1.39006769 1.81189601 2.64716828]
print(e.sum(axis=1)) #axis 1 ise satırları sum ile toplar     [2.26558847 1.32516564 2.38434531 3.59612532 3.08387866]


#-----------------------
#Indexing and Slicing
#-----------------------
import numpy as np
array = np.array([1,2,3,4,5,6,7]) #vector dimension = 1 yani 1 boyutlu
print(array[0:4]) #[1 2 3 4]
reversee_array = array[::-1]
print(reversee_array) #[7 6 5 4 3 2 1]
array1 = np.array ([[1,2,3,4,5],[6,7,8,9,10]]) # dimension = 2 yani 2 boyutlu
print(array1[1,2]) # ekrana 8 yazdırır 1.satır 2.sütundaki sayıyı yazdır (saymaya 0 dan başlar unutma unutuyosanda boş yere okul okuma zamanına yazık)
print(array1[1,1:4]) # ekrana [7 8 9] yazdırır 1. satırın 1,2,3. değerlerini yazdırdı


#-------------------------
#Shape Manipulation
#-------------------------
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])  #[[1 2 3]
                                             #[4 5 6]     çıktısı bu şekilde
                                             #[7 8 9]]
print(array)
#Flatten
a = array.ravel() # [1 2 3 4 5 6 7 8 9] çıktısı bu şekilde üç boyutlu halden tek boyutlu hale getirdi
print(a)
array2 = a.reshape(3,3)  #[[1 2 3]
                         #[4 5 6]     çıktısı bu şekilde eski haline getirdi aslında (3,3) yazarak 3 e 3 lük olsun istedik
                         #[7 8 9]]
print(array2)
#Transpoze
arrayT = array2.T        #[[1 4 7]
                         #[2 5 8]   çıktısı bu şekilde
                         #[3 6 9]]
print(arrayT)
#Reshape
array5 =np.array([[1,2],[3,4],[4,5]]) # 3 satır 2 stündan oluşan bir  matrix (array ile matrix aynı şey)
array5.reshape(2,3) # 2 satır 3 stün  yaptık
print(array5) #[[1 2]
              #[3 4]
              #[4 5]]
array5.resize(3,2) #[[1 2]
                   #[3 4]
                   #[4 5]]
print(array5)
#Resize ile Reshape arası fark Reshape ettimiz array değişmez Resize değiştir


#---------------------
#Stacking Arrays
#---------------------
#İki arrayi birleştirme
import numpy as np
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])
#Vertical yani dikey birleştime
array3 = np.vstack((array1,array2))
print(array3) #[[ 1  2]
              #[ 3  4]     çıktısı bu şekil
              #[-1 -2]
              #[-3 -4]]
#Horizontal yani yatay birleştime
array4 = np.hstack((array1,array2))
print(array4) #[[ 1  2 -1 -2]
              #[ 3  4 -3 -4]]  çıktısı bu şekil


#-----------------------
#Convert and Copy Array
#-----------------------
#Listeden arraye arrayden listeye dönüşüm yapma ve arraylerle ilgili küçük trickler
#Convert
import numpy as np
#Listeden numpy arraye geçme
liste = [1,2,3,4] #list
array = np.array(liste) #Numpy array
print(type(array)) #<class 'numpy.ndarray'>
print(array) #[1 2 3 4]
#Numpy arrayden liste geçme
list2 = list(array)
print(type(list2)) #<class 'list'>
print(list2) #[1, 2, 3, 4]
#Copy
a = np.array([1,2,3])
b = a.copy()
c = a.copy()
print(a,b,c) # a = [1 2 3] b = [1 2 3] c = [1 2 3]
b[0]=15
print(a,b,c) # a = [1 2 3] b =  [15  2  3] c =  [1 2 3]
# Sadece b[0] değiştirebildik copy yaptımızda memoryde alan ayırdık.


#------------------------
#Introduction to Pandas
#------------------------
import pandas as pd
dictionary = {"Name":["Ali","Ayşe","Baki","Simge"],
              "Age":[10,15,21,23],        #{'Name': ['Ali', 'Ayşe', 'Baki', 'Simge'], 'Age': ['10', '15', '21', '23'], 'Maas': ['100', '150', '999', '250']}
              "Maas":[100,150,999,250]}
print(dictionary)
dataFrame = pd.DataFrame(dictionary) #    Name Age Maas
                                     # 0    Ali  10  100
                                     # 1   Ayşe  15  150    Bu still excel yazış stili gibi daha düzenli
                                     # 2   Baki  21  999
                                     # 3  Simge  23  250
print(dataFrame)
head = dataFrame.head()   # Baştan ilk 5 veriyi verir
tail = dataFrame.tail()   # Sondan son 5 veriyi verir
head = dataFrame.head(15) # Baştan ilk 15 veriyi verir
tail = dataFrame.tail(15) # Sondan son 15 veriyi verir


#---------------------
#Pandas Basic Methods
#---------------------
import pandas as pd
dictionary = {"Name":["Ali","Ayşe","Baki","Simge"],
              "Age":[10,15,21,23],
              "Maas":[100,150,999,250]}
print(dictionary)
dataFrame = pd.DataFrame(dictionary)
print(dataFrame.columns)    # Columnsları yazdırır *Çıktısı*== Index(['Name', 'Age', 'Maas'], dtype='object')
print(dataFrame.info())     # DataFrame hakkında bilgi verir *Çıktısı*== 0   Name    4 non-null      object  1   Age     4 non-null      object  2   Maas    4 non-null      object
print(dataFrame.dtypes)     # DataFrame data tiplerinin ne olduğunu gösterir *Çıktısı*== Name    object      Age     object      Maas    object
print(dataFrame.describe()) # Sadece Numeric Featuresleri alır featuresin anlamı columns.


#-------------------------------------------
#Indexing and Slicing Data Frames In Pandas
#-------------------------------------------
import pandas as pd
dictionary = {"Name":["Ali","Ayşe","Baki","Simge"],
              "Age":[10,15,21,23],
              "Maas":[100,150,999,250]}
print(dictionary)
dataFrame = pd.DataFrame(dictionary)
print(dataFrame["Age"]) # 0    10
                        # 1    15
                        # 2    21
                        # 3    23
                        # Name: Age, dtype: object

print(dataFrame.Age)  # Bu şekildede verileri alabiliyoruz
#Feature ekleme
dataFrame["yeni_feature"] = [-1,-2,-3,-4]
print(dataFrame.yeni_feature) # 0   -1
                              # 1   -2
                              # 2   -3
                              # 3   -4
                              # Name: yeni_feature, dtype: int64


#----------------------------
#Filtering Pandas Data Frame
#----------------------------
import pandas as pd
dictionary = {"Name":["Ali","Ayşe","Baki","Simge","Veli","Dilara"],
              "Age":[10,15,21,23,45,"2],
              "Maas":[100,150,550,250,350,50]}
print(dictionary)
dataFrame = pd.DataFrame(dictionary)
# Maaşı 200 tl üzerinde olanları bul
filtre = dataFrame.Maas > "300"
print(filtre) # 0    False
              # 1    False
              # 2     True
              # 3     True
              # 4     True
              # 5     True
              # Name: Maas, dtype: bool
filtrelenmis_data = dataFrame[filtre]
print(filtrelenmis_data) #    Name Age Maas
                         # 2  Baki   21  550
                         # 3  Simge  23  250
                         # 4  Veli   45  350



#--------------------
#List Comprehension
#--------------------
import pandas as pd
dictionary = {"Name":["Ali","Ayşe","Baki","Asya","Atakan","Yasemin"],
              "Age":[10,15,21,28,42,53],
              "Maas":[100,150,900,250,350,550]}
print(dictionary)
dataFrame = pd.DataFrame(dictionary)
print(dataFrame.Maas)  # Maaşları yazdırır
ortalama_maas = dataFrame.Maas.mean()
print(ortalama_maas) # Maaş ortalamasını alır  383.3333333333333
# dataFrame yeni bir columns ekliyoruz elemanların aldığı maaşlar ortalamanın üzerinde mi altında mı onu yazdırıyor         #yuksek
dataFrame["maas_seviyesi"] = ["yuksek" if ortalama_maas > i else "dusuk" for i in dataFrame.Maas]                           #yuksek
for i in dataFrame.Maas:                                                                                                    #dusuk
  if(ortalama_maas > i ):                                                                                                   #yuksek
    print("yuksek")                                                                                                         #yuksek
  else:#dusuk
    print("dusuk")


#-------------------
#Concatenating Data
#-------------------
import pandas as pd
dictionary = {"Name":["Ali","Ayşe","Baki","Simge","Sefo","Cano","İbo","Ato"],
              "Age":[10,15,44,23,100,18,31,53],
              "Maas":[100,150,200,250,300,350,400,450]}
dataFrame = pd.DataFrame(dictionary)
dataFrame["yeni_feature"] = [-1,-2,-3,-4,-1,-2,-3,-4]
dataFrame.drop(["yeni_feature"],axis = 1 ) # axis = 1 ise yukardan aşşağıya drop eder axis = 0 ise soldan sağa drop ederdi drop etmek çıkarmak
print(dataFrame) # drop etmemize rağmen yeni future dataFrame de duruyor
dataFrame.drop(["yeni_feature"],axis = 1 ,inplace = True ) # inplace = True eşlemek gibi  dataFrame = dataFrame.drop(["yeni_feature"],axis = 1 ) gibi
print(dataFrame)
#dataFrame ilk 5 ve son 5  verileri alıpr horizontal ve vertical birleştirme
data1 = dataFrame.head()
data2 = dataFrame.tail()
#vertical
data_concat = pd.concat([data1,data2],axis = 0)
print(data_concat)
#horizontal
hMaas = dataFrame.Maas
hAge = dataFrame.Age
data_h_concat = pd.concat([hMaas,hAge],axis = 1)
print(data_h_concat)


#------------------
#Transforming Data
#------------------
import pandas as pd
dictionary = {"Name":["Ali","Ayşe","Baki","Simge","Sefo","Cano","İbo","Ato"],
              "Age":[10,15,44,23,100,18,31,53],
              "Maas":[100,150,200,250,300,350,400,450]}
dataFrame = pd.DataFrame(dictionary)
# Amaç yaşdaki verileri 2 ile çarpıp yeni bir columns oluşturma
dataFrame["çapık"] = [i*2 for i in dataFrame.Age]
print(dataFrame)
# Apply metodu ile
def carpik_columns(Age):
  return Age*2
dataFrame["carpik_columns"] = dataFrame.Age.apply(carpik_columns)
print(dataFrame)


#---------------
#Pandas Review
#---------------
#matplotlib kütüphanesi
#görselleştirme kütüphanesi
#line plot,scatter plot,bar plot,subplot,histogram göstercem

import pandas as pd
df = pd.read_csv("iris.csv") # iris.csv aynı klasörde olmalı iris.csv yazacaksak yoksa yolu kopyalayıp df = pd.read_csv("C:\User\user\Destop\iris.csv") olmalı
print(df.columns) # columsnları yazdırdık  Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species'],dtype='object')
print(df.Species) # türleri yazdırdık
print(df.Species.unique()) #  ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica'] 3 tür varmış  unique() benzersiz demek gibi bişey bir veri grubunda
#çok tekrar eden veriler varsa ve aralarında tek tük farklı veriler varsa kaç farklı veri oldunu görmek için kullanırız


#-----------
#Line Plot
#-----------
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris.csv")
df1 = df.drop(["Id"],axis=1) # pandas otomatik id numarası verdiği için bu datada id bölümünü kaldırıyoruz
#Görselleştirme
df1.plot()
plt.show() # her zaman konulmalı çizilen plotun gözükmesini sağlıyor
#iris.csv gösrselleştirme
#Visualization With Matplotlib Line Plot 1
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"] #özellikleri bir değişkene atadık
virginica = df[df.Species == "Iris-virginica"]
#Visualization With Matplotlib Line Plot 2
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa") # setosa PetalLengthCm mi Id sine göre x ve ye ekseni üzerinde görselleştircez
plt.legend() # labelin default değerini en uygun yere koymasını sağlıyor
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()
#Visualization With Matplotlib Line Plot 3
df1.plot(grid=True,alpha= 0.9) #grid ekranı karelere bölmesi alpha opasite yani saydamlık sıfıra yaklaşırsa saydamlık artar
plt.show()

#-----------
#Scatter Plot
#-----------
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]
# Visualization With Matplotlib Scatter Plot 1
plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

#-----------
# Histogram
#-----------
#Visualization With Matplotlib Histogram 1
plt.hist(setosa.PetalLengthCm,bins= 50)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

#-----------
# Bar Plot
#-----------
import numpy as np
#x = np.array([1,2,3,4,5,6,7])
#
#y = x*2+5
#
#plt.bar(x,y)
#plt.title("bar plot")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()

x = np.array([1,2,3,4,5,6,7])
a = ["turkey","usa","a","b","v","d","s"]
y = x*2+5

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#-----------
# Subplots
#-----------
#Visualization With Matplotlib Subplot 1
df1.plot(grid=True,alpha= 0.9,subplots = True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]
#Visualization With Matplotlib Subplot 2
plt.subplot(2,1,1) # 2 grafik olcak 1.satırım olcak 1.sini çiz demek gibi
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.ylabel("setosa -PetalLengthCm")
plt.subplot(2,1,2) # 2 grafik olcak 1.satırım olcak 2.sini çiz demek gibi
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.ylabel("versicolor -PetalLengthCm")
plt.show()