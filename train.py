import os
import shutil
from tkinter import Tk, filedialog
import subprocess

# Torch kontrolü
import torch
import torchvision
print("🔥 Torch sürümü:", torch.__version__)

# Input klasörü oluştur
os.makedirs("Input", exist_ok=True)

# Tkinter ile görsel seç
root = Tk()
root.withdraw()  # Tk penceresini gizle
img_path = filedialog.askopenfilename(
    title="Bir görsel seçin",
    filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")]
)
root.destroy()

if not img_path:
    raise Exception("❌ Görsel seçilmedi, işlem iptal edildi.")

# Input klasörüne kopyala
shutil.copy(img_path, f"Input/{os.path.basename(img_path)}")
img_name = os.path.basename(img_path)
print("🖼️ Seçilen ve kopyalanan görsel:", img_name)

# Eski modelleri sil
if os.path.exists("TrainedModels"):
    shutil.rmtree("TrainedModels")
    print("🗑️ Eski modeller silindi")

# SinGAN eğitimini başlat
print("🚀 Model eğitimi başlıyor...")
subprocess.run([
    "python", "SinGAN/main_train.py",
    "--input_name", img_name,
    "--input_dir", "Input",
    "--max_size", "250",
    "--num_layer", "5"
], check=True)

print("✅ Eğitim tamamlandı")
