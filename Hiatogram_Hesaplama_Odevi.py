#Abdulkadir Yayan 02105076051

# Gerekli kütüphaneler içe aktarılır.
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 'ray.jpg' adlı bir resim dosyasını siyah-beyaz (grayscale) olarak yükler.
resım = cv2.imread('ray.jpg', 0)

hist = np.zeros(256)
[w, h] = np.shape(resım)

for v in range(0, h):
    for u in range(0, w):
        i = resım[u, v]
        hist[i] = hist[i] + 1

# Piksel değerlerinin histogramını metin tabanlı olarak ekrana yazdırır.
for i in range(0, 256):
    print(i, "=", hist[i])
cv2.waitKey(0)
histHesapla = cv2.calcHist([resım], [0], None, [256], [0, 256])

plt.plot(hist, color='#000000')

# Grafiği ekranda gösterir.
plt.show()
