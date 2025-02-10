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

unique_lines = set()

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
                # d(resourceId="com.titantech.showmyipaddress:id/btn_recheckip").click()
                # d(resourceId="com.sec.android.app.launcher:id/iconview_titleView", text="TikTok").long_click()
                # d.press('home')
                # d.xpath('//*[@content-desc="Show My IP Address"]/android.widget.ImageView[1]').click()
                # time.sleep(5)
                # with open("proxy.txt", "r", encoding="utf-8") as file:
                #     for line in file:
                #         line = line.strip()
                #         if line and line not in unique_lines:
                #             d2.changeProxy(line)
                #             unique_lines.add(line)
                #             print(f"Thiết bị {device} thay đổi {line} thành công")
                # d.press('home')
                # d(resourceId="com.sec.android.app.launcher:id/iconview_titleView", text="TikTok").click()
                # d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/it8"]/android.widget.ImageView[1]').click()
                # d(resourceId="com.ss.android.ugc.trill:id/it8").click()
                # d(text="Hồ sơ").click()
                # d(text="Trang chủ").click()
                d.click(34,264)
                time.sleep(3)
                # time.sleep(9.0)
                # d.send_keys("Minrie Official")
                
                # # d(resourceId="com.ss.android.ugc.trill:id/mzx").click()
                # i = 0
                # while i < 3:
                #     d.swipe_ext("up", scale=0.8)
                #     time.sleep(8.0)
                #     i += 1
            except Exception as e:
                print(f"Lỗi khi kết nối thiết bị {device}: {e}")
        batdau(device)

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