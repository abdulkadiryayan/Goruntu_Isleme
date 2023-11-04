#Abdulkadir Yayan 02105076051

# Gerekli kütüphaneler içe aktarılır.
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 'aslan.jpg' adlı bir resim dosyasını siyah-beyaz (grayscale) olarak yükler.
fotograf = cv2.imread('aslan.jpg', 0)

# Bir dizi olan 'hist' oluşturulur ve 256 elemanlı olarak başlatılır.
# Bu dizi, görüntünün piksel değerlerinin histogramını tutmak için kullanılacaktır.
hist = np.zeros(256)

# Görüntünün boyutları 'w' ve 'h' değişkenlerine atanır.
[w, h] = np.shape(fotograf)

# İki iç içe döngü (for döngüleri) kullanılarak, her pikselin değeri alınır ve bu değere karşılık gelen histogram dizisinin ilgili elemanı artırılır.
# Bu, görüntünün piksel değerlerini tarayarak histogramı hesaplar.
for v in range(0, h):
    for u in range(0, w):
        i = fotograf[u, v]
        hist[i] = hist[i] + 1

# Piksel değerlerinin histogramını metin tabanlı olarak ekrana yazdırır.
for i in range(0, 256):
    print(i, "=", hist[i])

# Ekranda bir tuşa basılana kadar pencerenin açık kalmasını sağlar.
cv2.waitKey(0)

# Histogramın hesaplanması için OpenCV'nin 'cv2.calcHist' fonksiyonu kullanılır.
# Bu fonksiyon, 'fotograf' görüntüsündeki piksel değerlerinin histogramını hesaplar ve sonucu 'histHesapla' değişkenine kaydeder.
histHesapla = cv2.calcHist([fotograf], [0], None, [256], [0, 256])

# Histogram verilerini siyah renkte çizerek grafiği görselleştirir.
plt.plot(hist, color='#000000')

# Grafiği ekranda gösterir.
plt.show()
