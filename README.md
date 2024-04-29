# modules-generate-code-licence
```python
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
```
