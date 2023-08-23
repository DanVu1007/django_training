# Bước 1 – Cài đặt Django

### Tạo thư mục django-apps (hoặc bất kỳ tên nào khác) để chứa ứng dụng Django
```bash
mkdir django-apps
```
```bash
cd django-apps
```
### Ở trong thư mục django-apps, tạo môi trường ảo có tên env
```bash
composer clear-all
```
### Sau đó activate môi trường này:
```bash
. env/bin/activate
```
*Khi đã được activate thành công thì prompt sẽ có phần (env) ở phía trước:*
`(env) danva@aht.local@CAS-065`

### Bên trong môi trường này, ta sẽ cài đặt Django bằng pip:
```bash
. pip install django
```
### Sau đó kiểm tra xem Django đã được cài đặt thành công chưa:
```bash
. django-admin --version
```
`kết quả vậy là thành công`
`Output:`
`3.0.6`