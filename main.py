import os
import shutil
import subprocess

def generate_samples(img_name: str):
    print("10 ADET YENİ ÇİZİM ÜRETİLİYOR...")
    subprocess.run([
        "python", "SinGAN/random_samples.py",  # Düzeltildi: SinGAN klasörü altındaki dosya
        "--input_name", img_name,
        "--input_dir", "Input",
        "--mode", "random_samples",
        "--gen_start_scale", "0"
    ], check=True)

def zip_output():
    if os.path.exists("Output") and len(os.listdir("Output")) > 0:
        shutil.make_archive("SinGAN_Output", "zip", "Output")
        print("Output ZIP oluşturuldu: SinGAN_Output.zip")
    else:
        print("Output oluşmadı")

if __name__ == "__main__":
    img_name = "drawing.png"  # Eğitim sırasında kullanılan görsel
    generate_samples(img_name)
    zip_output()