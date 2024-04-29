"""
    # Copyright © 2022 By Nguyễn Phú Khương
    # ZALO : 0363561629
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""
import hashlib

def generate_license_key(rand:str):
    # Tạo mã giấy phép bằng mã băm SHA-512
    sha512 = hashlib.sha512()
    sha512.update(rand.encode())  # Thay "Your Unique Data Here" bằng dữ liệu độc nhất của bạn
    
    license_key = sha512.hexdigest()
    
    # Định dạng mã giấy phép thành chuỗi XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    formatted_key = '-'.join([license_key[i:i+5] for i in range(0, len(license_key), 5)])
    
    return formatted_key

# Tạo giấy phép
license_key = generate_license_key('abc')
print("Giấy phép ở dạng XXXXX-XXXXX-XXXXX-XXXXX-XXXXX:", license_key)
