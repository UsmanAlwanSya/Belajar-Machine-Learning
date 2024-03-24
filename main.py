import pandas as pd
import matplotlib.pyplot as plt

#upload dataset kopi arabika jawabarat
data = pd.read_csv("kopi_arabika_kabupatenkota_data.csv")

#lihat isi data  
data

#menampilkan 5 data teratas
data.head()

#menampilkan 5 data terakhir
data.tail()

#Melihat Tipe data
data.dtypes

#Menampilkan Informasi Dataset
print(data.info())




