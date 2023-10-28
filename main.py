from PIL import Image  # Pillow kütüphanesinden Image sınıfını içe aktar

import os  # Python işletim sistemi işlemleri için 'os' modülünü içe aktar

# 1. Kaynak klasörün adını 'source_folder' değişkenine ata
source_folder = "inputImg"

# 2. Hedef klasörün adını 'target_folder' değişkenine ata
target_folder = "outputImg"

# 3. Eğer 'target_folder' adlı klasör yoksa, oluştur
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 4. 'jpg_files' adlı liste, 'source_folder' klasöründe bulunan tüm dosyalar arasından sadece .JPG uzantılı olanları içerir
jpg_files = [file for file in os.listdir(source_folder) if file.endswith(".JPG")]

# 5. Her bir JPG dosyası için aşağıdaki işlemleri yap
for file_name in jpg_files:

    # 6. 'Image.open' ile JPG dosyasını aç
    with Image.open(os.path.join(source_folder, file_name)) as img:

        # 7. Hedef dosya adını belirle, .JPG uzantısını .webp ile değiştir
        target_file_name = file_name.replace(".JPG", ".webp")

        # 8. Hedef dosyanın tam yolunu belirle
        target_file_path = os.path.join(target_folder, target_file_name)

        # 9. Resmi WebP formatında ve belirli bir kalite seviyesi (quality=10) ile kaydet
        img.save(target_file_path, "webp", quality=10)

# 10. Tüm işlemler tamamlandığında "Finished!!" mesajını ekrana yazdır
print("Finished!!")
