import requests

API_KEY = "AeyKUdeuaIDNGXNgDquBnR"
URL = f'https://topproxy.vn/api/listproxy.php?key={API_KEY}&loaiproxy=FPT'

try:
    response = requests.get(URL)  # Gửi request với timeout

    # Kiểm tra status_code
    if response.status_code == 200:  # 200 nghĩa là request thành công
        try:
            http_proxies = response.json()  # Chuyển đổi JSON
            print(http_proxies)
        except ValueError:
            print("Lỗi: Phản hồi không phải là JSON hợp lệ.")
    else:
        print(f"Lỗi HTTP: {response.status_code} - {response.reason}")

except requests.exceptions.RequestException as e:
    print(f"Lỗi kết nối: {e}")
