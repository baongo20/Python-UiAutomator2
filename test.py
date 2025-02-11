import os,time
try:
    import threading, subprocess, base64, cv2, random, requests
    import numpy as np
except:
    os.system("pip install --force-reinstall --no-cache opencv-python")
    os.system("pip install numpy")
    os.system("pip install requests")
import threading, subprocess, base64, cv2, random, hashlib, sys, requests
import numpy as np
from datetime import datetime
from  xml.dom.minidom import parse
import re
import pyautogui

try:
    import uiautomator2 as u2
except:
    os.system("pip install uiautomator2")
import uiautomator2 as u2
from uiautomator2 import Direction
import concurrent.futures
import queue


class Auto:
    def __init__(self, handle):
        self.handle = handle

    def resetServer():
        """
        Reset Server ADB
        """
        subprocess.call("adb kill-server", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        time.sleep(2)
        subprocess.call("adb start-server", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        time.sleep(3)

    def check_wifi(self):
        result = subprocess.check_output(f'adb -s {self.handle} shell settings get global wifi_on', shell=True, text=True)
        return result.strip()

    def click(self, x, y):
        subprocess.Popen(f'adb -s {self.handle} shell input tap {x} {y}', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def swipe(self, x1, y1, x2, y2):
        subprocess.Popen(f"adb -s {self.handle} shell input touchscreen swipe {x1} {y1} {x2} {y2} 1000", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def back(self):
        subprocess.Popen(f"adb -s {self.handle} shell input keyevent 3", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def changeProxy(self, ip):
        """
        Input Proxy Http IP:PORT
        Thêm Proxy Http IP:PORT
        """
        subprocess.Popen(f'adb -s {self.handle} shell settings put global http_proxy {ip}', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def remProxy(self):
        """
        Input Proxy Http IP:PORT
        Thêm Proxy Http IP:PORT
        """
        subprocess.Popen(f'adb -s {self.handle} shell settings put global http_proxy :0', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # def delete_cache(self, package):
    #     subprocess.check_output(f"adb -s {self.handle} shell pm clear {package}", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # def off(self, package):
    #     subprocess.call(f"adb -s {self.handle} shell am force-stop {package}", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def input_text(self, text=None, VN=None):
        if text == None:
            text =  str(base64.b64encode(VN.encode('utf-8')))[1:]
            subprocess.call(f"adb -s {self.handle} shell ime set com.android.adbkeyboard/.AdbIME", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            subprocess.call(f"adb -s {self.handle} shell am broadcast -a ADB_INPUT_B64 --es msg {text}", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            return
        subprocess.Popen(f"adb -s {self.handle} shell input text '{text}'", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # def show_device(self, screen_width: int, screen_height: int, title: str):
    #     """Hiển thị điện thoại của bạn lên màn hình máy tính"""
    #     grid_rows = 2
    #     grid_cols = 5
    #     device_index = int(self.handle[-1], 16) % (grid_rows * grid_cols)
    #     col = device_index % grid_cols
    #     row = device_index // grid_cols
    #     window_width = screen_width // grid_cols
    #     window_height = screen_height // grid_rows
    #     x = col * window_width
    #     y = row * window_height
    #     subprocess.Popen([
    #         "scrcpy", "-s", self.handle,
    #         "--window-title", title,
    #         "--window-x", str(x), "--window-y", str(y),
    #         "--window-width", str(window_width), "--window-height", str(window_height)
    #     ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def get_devices():
    devices_output = subprocess.check_output("adb devices").decode("utf-8").strip().split("\n")[1:]
    devices = [line.split("\t")[0] for line in devices_output if "device" in line]
    return devices

devices_list = get_devices()
thread_count = len(devices_list)

class starts(threading.Thread):
    def __init__(self, device):
        super().__init__()
        self.device = device
       
    def run(self):
        device = self.device
        print(device)

        def batdau(device):
            try:
                d2 = Auto(device)
                d = u2.connect(device)
                if not d.info:  # Kiểm tra thiết bị có sẵn không
                    print(f"Thiết bị {device} không sẵn sàng.")
                    return
                print(f"Thiết bị {device} có {d2.check_wifi()}")
            except Exception as e:
                print(f"Lỗi khi kết nối thiết bị {device}: {e}")
        batdau(device)

class Controller:
    def __init__(self, device_id=None):
        self.device = u2.connect(device_id)
        print(f"Đã kết nối với thiết bị: {self.device.info['serial']}")

    def unlock_device(self):
        """Mở khóa màn hình nếu đang tắt."""
        if self.device.info['screenOn'] is False:
            self.device.screen_on()
            print("Màn hình đã được bật.")

    def open_app(self, package_name):
        """Mở ứng dụng theo tên gói (package name)."""
        self.device.app_start(package_name)
        print(f"Đã mở ứng dụng: {package_name}")
        time.sleep(2)

    def click_element(self, resource_id):
        """Tìm và nhấn vào một phần tử theo resource-id."""
        if self.device(resourceId=resource_id).exists(timeout=5):
            self.device(resourceId=resource_id).click()
            print(f"Đã nhấn vào phần tử: {resource_id}")
        else:
            print(f"Không tìm thấy phần tử: {resource_id}")

    def input_text(self, resource_id, text):
        """Nhập văn bản vào ô nhập liệu."""
        if self.device(resourceId=resource_id).exists(timeout=5):
            self.device(resourceId=resource_id).set_text(text)
            print(f"Đã nhập văn bản vào {resource_id}: {text}")
        else:
            print(f"Không tìm thấy ô nhập liệu: {resource_id}")

    def take_screenshot(self, filename="screenshot.png"):
        """Chụp ảnh màn hình và lưu lại."""
        self.device.screenshot(filename)
        print(f"Ảnh chụp màn hình đã lưu: {filename}")

    def scroll_down(self):
        """Cuộn xuống trong ứng dụng."""
        self.device.swipe(500, 1500, 500, 500)
        print("Đã cuộn xuống.")

    def close_app(self, package_name):
        """Đóng ứng dụng theo package name."""
        self.device.app_stop(package_name)
        print(f"Đã đóng ứng dụng: {package_name}")

    def disconnect(self):
        """Ngắt kết nối với thiết bị."""
        self.device.service("uiautomator").stop()
        print("Đã ngắt kết nối với thiết bị.")

# Main method
def main(m):
    device = devices_list[m]
    run = starts(device)
    run.start()  # Sửa lại từ run.run() thành run.start()

threads = []

for m in range(thread_count):
    t = threading.Thread(target=main, args=(m,))
    t.start()
    threads.append(t)

# Đợi tất cả luồng hoàn thành
for t in threads:
    t.join()