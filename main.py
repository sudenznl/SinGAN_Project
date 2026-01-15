import os
import subprocess
import shutil

# Görsel adı
img_name = "drawing.png"

# Output klasörü
os.makedirs("Output", exist_ok=True)

# TrainedModels klasörünü kontrol et
model_dir = f"TrainedModels/{os.path.splitext(img_name)[0]}"
if not os.path.exists(model_dir):
    raise FileNotFoundError("Model bulunamadı! Önce train.py çalıştırın.")

# Output içi temizle
for f in os.listdir("Output"):
    f_path = os.path.join("Output", f)
    if os.path.isfile(f_path):
        os.remove(f_path)
    else:
        shutil.rmtree(f_path)

# 10 rastgele örnek üret
print("10 ADET BENZER GÖRSEL ÜRETİLİYOR...")
subprocess.run([
    "python", "SinGAN/random_samples.py",
    "--input_name", img_name,
    "--input_dir", "Input",
    "--mode", "random_samples",
    "--gen_start_scale", "0",
    "--not_cuda"
], check=True)

# Output içi dosyaları modelden alıp Output klasörüne kopyala
# SinGAN otomatik olarak Output oluşturmaz, random_samples.py modelden görselleri kaydetmezse
# Bu yüzden TrainedModels içinden görselleri Output'a taşı
sample_dir = f"TrainedModels/{os.path.splitext(img_name)[0]}/RandomSamples"
if os.path.exists(sample_dir):
    for f in os.listdir(sample_dir):
        shutil.copy(os.path.join(sample_dir, f), "Output")

# ZIP oluştur
if os.path.exists("Output") and len(os.listdir("Output")) > 0:
    shutil.make_archive("SinGAN_Output", "zip", "Output")
    print("Output ZIP oluşturuldu: SinGAN_Output.zip")
else:
    print("Output oluşmadı")