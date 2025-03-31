# 🔐 AES File Encryption Tool (CBC Mode)  
> Simple & Secure File Encryption using Python 🐍 + AES (CBC)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 รายละเอียดโปรเจกต์ | Project Overview (TH/EN)

🔸 โปรแกรมนี้ใช้สำหรับ **เข้ารหัส (Encrypt)** และ **ถอดรหัส (Decrypt)** ไฟล์ เช่น `.jpg`, `.txt`, `.pdf`  
ด้วยอัลกอริธึม **AES (CBC Mode)** ซึ่งมีความปลอดภัยระดับสูง  
ผู้ใช้สามารถาเลือกไฟล์จากเมนู ไม่ต้องพิมพ์ชื่อเอง

🔸 This project is a simple **file encryption/decryption tool** using Python AES (CBC).  
Users can choose files via an auto menu instead of typing file names manually.

---

## 📁 โครงสร้างโปรเจกต์ | Project Structure

```
aes_file_encryption/
├── main.py                 # 🔧 โปรแกรมหลัก
├── .env                    # 🔑 เก็บ SECRET_KEY และ IV (ห้าม push ขึ้น GitHub)
├── .gitignore              # 🙈 กันไฟล์ไม่ให้ถูก push
├── README.md               # 📘 คำอธิบายโปรเจกต์
├── requirements.txt        # 📦 รายชื่อไลบรารีที่ใช้
│
├── test.jpg                # 🖼 ไฟล์ตัวอย่าง (ก่อนเข้ารหัส)
├── test.jpg.bin            # 🔐 ไฟล์ที่เข้ารหัสแล้ว
├── test.jpg_decrypted      # 🔓 ไฟล์หลังถอดรหัส
└── venv/                   # 🧪 Virtual Environment (ไม่ควร push)
```

---

## 🚀 วิธีใช้งาน | How to Use

### 1️⃣ ติดตั้งไลบรารี

```bash
pip install -r requirements.txt
```

### 2️⃣ สร้างไฟล์ `.env`

```env
SECRET_KEY=thisisaverysecretkey123456789101
IV=thisisasecretiv1
```

> 🔐 Key = 32 bytes | IV = 16 bytes

### 3️⃣ เริ่มรันโปรแกรม

```bash
python main.py
```

---

## 🥪 วิธีทดสอบ | How to Test

1. วางไฟล์ `.jpg` หรือ `.txt` ที่ต้องการเข้ารหัสไว้ในโฟลเดอร์
2. รัน `main.py` แล้วเลือก `1` เพื่อเข้ารหัส
3. จะได้ไฟล์ `.bin`
4. รันอีกครั้ง เลือก `2` เพื่อถอดรหัสไฟล์ `.bin`
5. โปรแกรมจะสร้างไฟล์ `_decrypted` ขึ้นมา

---

## ✅ ฟีเจอร์เด่น | Features

- 🔐 AES-256 CBC Mode: ความปลอดภัยระดับสูง
- 🗃️ เมนูเลือกไฟล์: ลดการพิมพ์ผิด
- 🔑 โหลด KEY/IV จาก `.env`
- 📁 แยกไฟล์ `.bin` และ `_decrypted` อย่างชัดเจน
- 🥪 พร้อมต่อยอด GUI / Web App

---

## 📸 ตัวอย่างหน้าจอ | Screenshot

> (แนบภาพ demo ได้ที่นี่ เช่น `images/demo.png`)

```markdown
![demo](images/demo.png)
```

---

## 🙋‍♀️ ผู้พัฒนา | Developer

**Beam (Sotidacho)**  
🌐 GitHub: [https://github.com/Sotidacho](https://github.com/Sotidacho)

หากคุณชอบโปรเจกต์นี้ กด ⭐ ที่ repo เพื่อเป็นกำลังใจได้เลย 😊

---

## 📜 License

Distributed under the **MIT License**  
See `LICENSE` file for more information.
