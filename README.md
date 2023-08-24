README ấn ctr+shift+v sẽ ra preview của README
# Bước 1 – Cài đặt Django

### Tạo thư mục django-apps (hoặc bất kỳ tên nào khác) để chứa ứng dụng Django
```
mkdir django-apps
```
```
cd django-apps
```
### Ở trong thư mục django-apps, tạo môi trường ảo có tên env
```
composer clear-all
```
### Sau đó activate môi trường này:
```
. env/bin/activate
```
### tắt activate môi trường:
```
deactivate
```
*Khi đã được activate thành công thì prompt sẽ có phần (env) ở phía trước:*
`(env) danva@aht.local@CAS-065`

### Bên trong môi trường này, ta sẽ cài đặt Django bằng pip:
```
pip install django
```
### Sau đó kiểm tra xem Django đã được cài đặt thành công chưa:
```
django-admin --version
```
`kết quả vậy là thành công`
`Output:`
`3.0.6`


# Bước 2 – Thay đổi cấu hình tường lửa

### Đối với tường lửa UFW, ta có thể chạy lệnh dưới đây để mở một port:
```
sudo ufw allow 8000
```

# Bước 3 – Khởi động project

### Tạo một ứng dụng
Bây giờ ta có thể khởi tạo một ứng dụng bằng django-admin – một công cụ command line cho các tác vụ quản trị trong Python. Sau đó dùng lệnh `startproject` để tạo một cấu trúc thư mục project cho website.
Chạy lệnh sau trong thư mục `django-apps`:
cd to `django-apps`
```
django-admin startproject testsite
```
Lưu ý: Khi chạy lệnh django-admin startproject <projectname>, cả thư mục project và package project đều sẽ có tên là <projectname>. Ngoài ra lệnh cũng tạo một project trong thư mục mà lệnh được chạy. Nếu có tham số <destination> trong lệnh thì Django sẽ sử dụng thư mục đích được chỉ định làm thư mục project, đồng thời tạo manage.py và package project bên trong đó.
Trong đó:
    `__init__.py` khởi tạo project Python
    `asgi.py` chứa cấu hình phần deploy của Asynchronous Server Gateway Interface (ASGI), cung cấp một tiêu chuẩn cho các ứng dụng đồng bộ hoặc không đồng bộ.
    `settings.py` mô tả cấu hình cài đặt của Django, cho phép Django biết thiết lập nào đang khả dụng.
    `urls.py` chứa một danh sách urlpatterns, có nhiệm vụ định tuyến và ánh xạ URL vào các views tương ứng.
    `wsgi.py` chứa cấu hình cho Web Server Gateway Interface (WSGI), cung cấp một tiêu chuẩn cho các ứng dụng Python đồng bộ.
    Người dùng có thể thay đổi file asgi.py hoặc wsgi.py để phù hợp với nhu cầu deploy của mình.

### Tạo một module
```
python3 manage.py startapp polls
```

# Bước 4 – Cấu hình Django

### Thêm địa chỉ IP vào danh sách ALLOWED_HOSTS
Vào thư mục sau ` ~/django-apps/testsite/testsite/settings.py`
Sửa nội dung:
'your-server-ip' thành 127.0.0.1
`Edit the line below with your server IP address
ALLOWED_HOSTS = ['your-server-ip']
...`

### Thêm địa chỉ IP vào danh sách ALLOWED_HOSTS
```
python3 manage.py createsuperuser
```
# Bước 5 – Truy cập ứng dụng web Django

Sau khi cấu hình xong, chuyển về thư mục chứa file manage.py:
```
cd ~/django-apps/testsite/
```
Sau đó chạy lệnh dưới đây, trong đó thay your-server-ip thành địa chỉ IP tương ứng của server:
```
python3 manage.py runserver your-server-ip:8000
```