import string
import re

# Alphabet yang sama dengan chall.py
alphabet = string.ascii_letters + "0123456789{}_"

# Baca flag.html
with open("flag.html", "r") as f:
    html = f.read()

# Extract semua hex colors
colors = re.findall(r'background:(#[0-9a-f]{6})', html)

# Target color (pure green)
TARGET = "#00ff00"

# Hitung jumlah kolom per baris (panjang alphabet)
cols = len(alphabet)

# Decode flag
flag = []
row_num = 0
for i in range(0, len(colors), cols):
    row = colors[i:i+cols]
    
    # Cari apakah ada target color di baris ini
    if TARGET in row:
        # Temukan posisi kolom
        col_pos = row.index(TARGET)
        # Convert ke karakter
        char = alphabet[col_pos]
        flag.append(char)
        print(f"Row {row_num}: Found '{char}' at column {col_pos}")
    
    row_num += 1

# Print flag
print("\n" + "="*50)
print("FLAG FOUND:")
print(''.join(flag))
print("="*50)
