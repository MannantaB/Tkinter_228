# Mengimpor tkinter sebagai pustaka GUI utama untuk membuat aplikasi desktop
import tkinter as tk
# Messagebox untuk menampilkan kotak pesan (pop-up).
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try: 
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat jendela utama root dengan judul “Aplikasi Prediksi Prodi Pilihan” dan ukuran 500x600 piksel.
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
# Untuk mengatur warna latar belakang
root.configure(bg="#d1c09f")

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#d1c09f",fg="#9e6c42")
judul_label.pack(pady=20)

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#d1c09f")
frame_input.pack(pady=10)

entries = []
# Menambahkan 10 label (Nilai Mata Pelajaran 1 hingga Nilai Mata Pelajaran 10) dan entry untuk setiap mata pelajaran. Setiap entry disimpan di list entries untuk diakses di fungsi hasil_prediksi.
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12),bg= "#d1c09f",fg="#61432a")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12),fg="#61432a")
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Membuat tombol prediksi_button untuk memicu fungsi hasil_prediksi saat ditekan. Tombol ini memiliki teks "Hasil Prediksi".
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#9e6c42", fg="white")
prediksi_button.pack(pady=30)

# Hasil_label digunakan untuk menampilkan hasil prediksi setelah input divalidasi.
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="#9e6c42",bg= "#d1c09f")
hasil_label.pack(pady=20)

# Untuk menjalankan GUI dan menunggu interaksi pengguna.
root.mainloop()