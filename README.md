## Hướng dẫn cài đặt và chạy dự án

### Yêu cầu hệ thống
- Python 3.8 hoặc mới hơn
- pip (trình quản lý gói Python)

### Cài đặt
1. Clone repository về máy:
   ```bash
   git clone <repository-url>
   cd object_detection_yolo

### Tạo môi trường ảo
```terminal
python -m venv venv
source venv/bin/activate  # Trên Linux/MacOS
venv\Scripts\activate     # Trên Windows
```

### Cài đặt các thư viện cần thiết
```
pip install -r requirements.txt
```

### Chạy chương trình
```
python detect.py
```