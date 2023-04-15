import os
import cv2
import pytesseract
from PIL import Image

#akses ke folder yang berisi hasil gambar
folder_path = 'C:/Users/hp/Documents/Proposal PA/preprocessing/Bahan Gambar Meteran'

#Loop untuk membaca setiap file gambar di folder
for filename in os.listdir(folder_path):
    img_path = os.path.join(folder_path, filename)
    img =cv2.imread(img_path)
    # Mengabaikan file yang bukan gambar
    if not filename.endswith('.jpeg'):
        continue

    #membaca file gambar menggunakan PIL
    image_path = os.path.join(folder_path, filename)
    image = Image.open(image_path)

    #konversi grayscale dan otsu threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape
    mean_pixel = cv2.mean(gray)
    contrast = (gray - mean_pixel[0]) / (mean_pixel[0])
    brightness = (mean_pixel[0]) / 255

    #konversi threshold
    #menjalankan OCR pada gambar yang telah diolah
    text =pytesseract.image_to_string(image)

    #menampilkan hasil ekstrak ke teks
    print('File:',filename)
    print("Hasil output:",text)
