# Pekerti
Research Activity to predict specialization

# To do list :
## 1. Clustering
- **ea.ipynb** = mengkluster mata kuliah prasyarat dari peminatan EA dan mengelompokan menjadi 2 cluster, yaitu cocok dan tidak cocok
- **cluster.ipynb** = mengkluster seluruh mahasiswa 2016 dan mengelompokannya kedalam 6 peminatan langsung
- **cluster v1.ipynb** = mengkluster setiap mata kuliah prasayat dan membuatnya menjadi matriks, setiap mahasiswa cocok di peminatan apa saja. ( jika 1, maka cocok )
- **cluster-mean.ipynb** = membuat scatter plot dari rata rata mata kuliah prasyarat

## 2. Silhouette Score
- **silhoette-score** = Melihat score silhouette dari setiap cluster peminatan

## 3. Clustering 2017
- **clustering 2017.ipynb** = melihat plot berapa banyak mahasiswa yang cocok dan tidak cocok pada angkatan tersebut

## 4. Tensorflow
- **tensorflow.ipynb** = implementasi tensorflow cnn untuk mengetahui 2017 kemungkinan lulus tepat waktu atau tidak

## 5. Seleksi Peminatan dan Lulus tepat waktu
- 2016 -> pilihan 1 pilihan 2 peminatan
- 2017 diprediksi peminatan mana berdasarkan 2016 termasuk pilihan 1 pilihan 2
- berdasarkan hasil peminatan 2017, diprediksi lulus tepat waktu atau engga dari 2016. nilai prasyarat + peminatannya
