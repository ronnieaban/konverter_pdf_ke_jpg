# PDF ke JPG Converter

Aplikasi Python untuk mengkonversi file PDF menjadi gambar JPG dengan kualitas tinggi.

## Fitur Utama
- Mengkonversi PDF multi-halaman menjadi gambar JPG individual
- Kualitas output tinggi dengan DPI yang dapat disesuaikan (default: 300)
- Menangani file PDF yang rusak atau tidak valid dengan pesan error yang jelas
- Menyimpan gambar dengan nama file yang sesuai urutan halaman

## Persyaratan Sistem
- Python 3.6 atau lebih baru
- PyMuPDF (fitz)
- Pillow (PIL)

## Instalasi

1. Clone repository ini atau download source code
2. Masuk ke direktori proyek:
   ```bash
   cd pdf_to_jpg_converter
   ```
3. Install dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

## Penggunaan

Format perintah:
```bash
python main.py input.pdf output_folder
```

Parameter:
- `input.pdf`: Path ke file PDF yang akan dikonversi
- `output_folder`: Direktori untuk menyimpan gambar JPG

Contoh:
```bash
python main.py dokumen.pdf ./hasil_gambar
```

## Output
- Gambar akan disimpan dengan format `[nama_file]_page1.jpg`, `[nama_file]_page2.jpg`, dst.
- Gambar output akan memiliki kualitas tinggi (300 DPI secara default)

## Penanganan Error
Aplikasi akan menampilkan pesan error untuk:
- File PDF yang tidak valid
- File input yang tidak ditemukan
- Masalah permission
- File PDF yang rusak

## Berkontribusi
Kontribusi untuk proyek ini sangat diterima. Berikut cara berkontribusi:
1. Fork repository ini
2. Buat branch baru (`git checkout -b fitur-baru`)
3. Commit perubahan Anda (`git commit -am 'Menambahkan fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## Lisensi
Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

## Kontak
Untuk pertanyaan atau masukan, silakan hubungi:
- Email: [alamat@email.com]
- GitHub: [username_github]
