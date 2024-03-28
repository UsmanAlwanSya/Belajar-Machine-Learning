import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('titanic.csv')

#Menampilkan Data 20 ke atas
data.head(20)

#Menampilakn Data 20 Kebawah
data.tail(20)

#Melakukan analisis Dengan Groub by kolom 'Sex' dan Kolom 'Survived'
survived_gender = data.groupby("Sex")["Survived"].sum()

#Memvisualisasikan Perbandingan Jumlah Survived berdasarkan Gender
plt.figure(figsize=(8, 6))
survived_gender.plot(kind='bar', color=['blue', 'pink'])
plt.title('Perbandingan Jumlah Penumpang yang Selamat berdasarkan Gender')
plt.xlabel('Gender')
plt.ylabel('Jumlah Penumpang Selamat')
plt.xticks(rotation=0)  # Untuk memperjelas label sumbu x
plt.show()
