import pandas as pd

#upload dataset kopi arabika jawabarat
data = pd.read_csv("kopi_arabika_kabupatenkota_data.csv")

#lihat isi data  
data

#menampilkan 5 data teratas
data.head()

#menampilkan 5 data terakhir
data.tail()
