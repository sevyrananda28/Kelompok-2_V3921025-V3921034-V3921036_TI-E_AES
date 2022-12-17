# import AES
from Crypto.Cipher import AES

# enkripsi key
key = b'prakskd         '

# buat instance cipher baru
cipher = AES.new(key, AES.MODE_EAX)

# data yang akan dienkripsi
data = "Kelompok2 AES".encode()

# nonce adalah nilai acak yang dihasilkan setiap kali kita membuat cipher menggunakan new()
nonce = cipher.nonce

# mengenkripsi data
ciphertext = cipher.encrypt(data)

# mencetak data terenkripsi
print("Cipher text:", ciphertext)

# menghasilkan instance baru dengan kunci dan nonce yang sama dengan cipher enkripsi
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

# mendekripsi data
plaintext = cipher.decrypt(ciphertext)
print("Decrypt text:", plaintext)