## 🔍 Gemini Pattern Predictor 🧩
 
Gemini Pattern Predictor adalah aplikasi CLI berbasis Python yang memanfaatkan kekuatan Google Gemini AI untuk memprediksi pola berikutnya dari rangkaian karakter.
Aplikasi ini cocok digunakan oleh developer, peneliti, atau siapa saja yang tertarik dalam eksplorasi pattern recognition dengan AI.

## ✨ Fitur Utama
* 🔤 Prediksi pola tunggal dan multiple (banyak pola sekaligus)
* 🤖 Integrasi dengan Google Gemini AI
* 📊 Analisis lengkap: prediksi, penjelasan, confidence level
* 💾 Simpan hasil analisis dalam format JSON
* 🧹 Validasi input otomatis dengan saran perbaikan

![Demo](img/Screenshot%202025-08-02%20154335.png)

## ⚙️ Instalasi
1. ### Clone repository
```bash
git clone https://github.com/nama_pengguna_anda/nama_repo_anda.git
```

2. ### Buka folder
```bash
cd pattern-predictor
```

3. ###  Konfigurasi API Key
* Buat file .env di root folder
* Tambahkan baris berikut dengan API key milikmu:
  **GEMINI_API_KEY=YOUR_API_KEY_HERE**

4. ### Install dependencies
``` bash
pip install -r requirements.txt
```

## 🚀 Cara Penggunaan
### Jalankan aplikasi
``` bash
python main.py
```

### Navigasi menu
1. Prediksi pola tunggal
2. Prediksi multiple pola
3. Keluar

### Contoh input
```bash
\\11||22\\33||
```

### Contoh output
```bash
🔄 Menganalisis pola...
🔍 ANALISIS POLA
================
📥 Input Pola: \11||22\33||
🎯 Prediksi Selanjutnya: 44
📊 Tingkat Kepercayaan: 95%
📝 Penjelasan: Pola tersebut menunjukkan urutan angka yang berulang.  Setiap angka diikuti oleh dirinya sendiri, kemudian dipisahkan oleh dua garis vertikal ('||').  Angka tersebut meningkat secara berurutan.  Oleh karena itu, angka selanjutnya dalam urutan adalah 4, diikuti oleh dirinya sendiri.
📋 Contoh Pola Lengkap: \11||22\33||44
⏰ Timestamp: 2025-08-02 16:10:27
```

## 🧰 Tech Stack
* Bahasa: Python 3.10+
* AI API: Google Generative AI (gemini-1.5-flash)
* Environment: dotenv
* Parsing & Format: JSON, Regex

