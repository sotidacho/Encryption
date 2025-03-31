from Crypto.Cipher import AES
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY").encode('utf-8')
IV = os.getenv("IV").encode('utf-8')


def encrypt_data(data: bytes) -> bytes:
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
    padding = 16 - (len(data) % 16)
    data += bytes([padding]) * padding
    return cipher.encrypt(data)


def decrypt_data(encrypted_data: bytes) -> bytes:
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
    decrypted_data = cipher.decrypt(encrypted_data)
    padding = decrypted_data[-1]
    return decrypted_data[:-padding]


def list_files(extension: str):
    return [f for f in os.listdir() if f.endswith(extension)]


def select_file(file_list: list):
    if not file_list:
        print("❌ ไม่มีไฟล์ที่ตรงกับเงื่อนไข")
        return None
    print("🔽 เลือกไฟล์:")
    for i, f in enumerate(file_list, 1):
        print(f"{i}. {f}")
    choice = input("🔸 เลือกหมายเลขไฟล์: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(file_list)):
        print("❌ ตัวเลือกไม่ถูกต้อง")
        return None
    return file_list[int(choice) - 1]


def encrypt_mode():
    jpg_files = list_files(".jpg")
    input_file = select_file(jpg_files)
    if not input_file:
        return
    output_file = input_file + ".bin"
    with open(input_file, "rb") as f:
        data = f.read()
    encrypted = encrypt_data(data)
    with open(output_file, "wb") as f:
        f.write(encrypted)
    print(f"✅ เข้ารหัสเสร็จสิ้น: {output_file}")


def decrypt_mode():
    bin_files = list_files(".bin")
    input_file = select_file(bin_files)
    if not input_file:
        return
    output_file = input_file.replace(".bin", "_decrypted")
    with open(input_file, "rb") as f:
        data = f.read()
    decrypted = decrypt_data(data)
    with open(output_file, "wb") as f:
        f.write(decrypted)
    print(f"✅ ถอดรหัสเสร็จสิ้น: {output_file}")


if __name__ == "__main__":
    print("🔹 เลือกโหมดที่ต้องการ:")
    print("1. เข้ารหัสไฟล์ (Encrypt)")
    print("2. ถอดรหัสไฟล์ (Decrypt)")
    choice = input("🔸 กรุณาเลือก (1 หรือ 2): ").strip()
    if choice == "1":
        encrypt_mode()
    elif choice == "2":
        decrypt_mode()
    else:
        print("❌ ตัวเลือกไม่ถูกต้อง")
