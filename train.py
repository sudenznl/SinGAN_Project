import os
import subprocess
import shutil

# Eğitilecek görsel (proje klasörüne koy)
img_name = "drawing.png"

# Input klasörü
os.makedirs("Input", exist_ok=True)

# Eğer görsel Input içinde yoksa kopyala
if not os.path.exists(f"Input/{img_name}"):
    if not os.path.exists(img_name):
        raise FileNotFoundError(f"{img_name} bulunamadı! Proje klasörüne koyun.")
    shutil.copy(img_name, f"Input/{img_name}")

# TrainedModels klasörünü oluştur
os.makedirs("TrainedModels", exist_ok=True)

# Eğer daha önce eğitilmiş model yoksa eğit
model_dir = f"TrainedModels/{os.path.splitext(img_name)[0]}"
if not os.path.exists(model_dir):
    print("Eğitim başlatılıyor...")
    subprocess.run([
        "python", "SinGAN/main_train.py",
        "--input_name", img_name,
        "--input_dir", "Input",
        "--max_size", "250",
        "--num_layer", "5",
        "--not_cuda"
    ], check=True)
    print("Eğitim tamamlandı!")
else:
    print("Model zaten var, yeniden eğitim yapılmayacak.")
