# 🔐 AES File Encryption Tool (CBC Mode)  
> Simple & Secure File Encryption using Python 🐍 + AES (CBC)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 รายละเอียดโปรเจกต์

เครื่องมือนี้ใช้สำหรับ **เข้ารหัส** และ **ถอดรหัสไฟล์** (เช่น .jpg, .txt ฯลฯ) โดยใช้  
**Advanced Encryption Standard (AES)** ในโหมด **CBC (Cipher Block Chaining)**  
พร้อมฟังก์ชันเลือกไฟล์จากเมนูอัตโนมัติผ่าน Terminal

---

## 📁 โครงสร้างโปรเจกต์
<pre> aes_file_encryption/ ├── main.py # 🔧 ไฟล์หลักที่ใช้เข้ารหัส/ถอดรหัสไฟล์ด้วย AES CBC ├── .env # 🗝 เก็บ SECRET_KEY และ IV (ห้าม push ขึ้น GitHub) ├── .gitignore # 🙈 ไฟล์ที่ระบุสิ่งที่ไม่ต้องการให้ Git จัดเก็บ ├── README.md # 📘 คำอธิบายโปรเจกต์ ├── requirements.txt # 📦 รายชื่อไลบรารี Python ที่ใช้ │ ├── test.jpg # 🖼 ไฟล์ตัวอย่าง (ก่อนเข้ารหัส) ├── test.jpg.bin # 🔐 ไฟล์ที่เข้ารหัสแล้ว ├── test.jpg_decrypted # 🔓 ไฟล์หลังถอดรหัส │ └── venv/ # 🧪 Python Virtual Environment (ไม่ควร push ขึ้น Git) </pre>

