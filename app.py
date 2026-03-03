from PIL import Image
import os

# Fungsi untuk mencari file gambar otomatis
def cari_gambar(nama_file):
    # Coba cari di folder tempat script ini berada
    if os.path.exists(nama_file):
        return nama_file
    # Coba cari di folder Download (lokasi umum di Android)
    path_download = "/storage/emulated/0/Download/" + nama_file
    if os.path.exists(path_download):
        return path_download
    return None

def dokter_tanaman(nama_file):
    path_gambar = cari_gambar(nama_file)
    
    if path_gambar is None:
        print(f"❌ ERROR: Gambar '{nama_file}' tidak ketemu!")
        print("Pastikan file ada di folder 'Download' HP kamu.")
        return

    print(f"📸 Menganalisa gambar...")
    
    try:
        img = Image.open(path_gambar)
        img = img.convert('RGB')
        # Kecilkan gambar biar HP tidak lemot (Resize)
        img = img.resize((100, 100)) 
        lebar, tinggi = img.size
    except:
        print("Gagal membuka gambar.")
        return

    pixel_sehat = 0
    pixel_sakit = 0
    total_pixel = 0

    # Scanning Pixel (Sekarang ukurannya 100x100, jadi cepat)
    for x in range(lebar):
        for y in range(tinggi):
            r, g, b = img.getpixel((x, y))
            
            # Abaikan background putih/hitam
            if sum((r,g,b)) < 50 or sum((r,g,b)) > 700:
                continue 

            total_pixel += 1

            # Logika Hijau vs Merah
            if g > r and g > b:
                pixel_sehat += 1
            else:
                pixel_sakit += 1

    if total_pixel == 0:
        print("Gambar kosong / tidak jelas.")
        return

    persen_sakit = (pixel_sakit / total_pixel) * 100
    
    print("-" * 20)
    print(f"Kerusakan: {persen_sakit:.1f}%")
    
    if persen_sakit < 10:
        print("✅ Tanaman SEHAT!")
    elif persen_sakit < 40:
        print("⚠️ WASPADA! Ada sakit.")
    else:
        print("🚑 BAHAYA! Butuh obat.")
    print("-" * 20)

# Jalankan program
dokter_tanaman("daun.jpg")
