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


class Auto:
    def __init__(self, device_id=None):
        self.device = u2.connect(device_id)
        print(f"Đã kết nối với thiết bị: {self.device.info['serial']}")

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
            # time.sleep(random.uniform(0.08, 0.3))
            print(f"Đã nhập văn bản vào {resource_id}: {text}")
        else:
            print(f"Không tìm thấy ô nhập liệu: {resource_id}")

    def scroll_down(self):
        """Cuộn xuống trong ứng dụng."""
        self.device.swipe(500, 1500, 500, 500)
        print("Đã cuộn xuống.")

    def close_app(self, package_name):
        """Đóng ứng dụng theo package name."""
        self.device.app_stop(package_name)
        print(f"Đã đóng ứng dụng: {package_name}")

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
        print(f"Khởi chạy cho thiết bị: {self.device}")
        try:
            d = u2.connect(self.device)
            if not d.info:
                print(f"Thiết bị {self.device} không sẵn sàng.")
                return
            
            # launch app if not running, skip launch if already running
            sess = d.session("com.ss.android.ugc.trill", attach=True)
            time.sleep(10.0)

            # swipe 10 videos
            i = 1
            while i <= 4:
                d.swipe_ext('up', scale=random.uniform(0.8, 1.0))
                time.sleep(random.randint(5, 10))
                i += 1

            # likes video và xem bình luận
            if d(resourceId="com.ss.android.ugc.trill:id/dt4").exists():
                d(resourceId="com.ss.android.ugc.trill:id/dt4").click()
                time.sleep(5.0)
                d(resourceId="com.ss.android.ugc.trill:id/cos").click()
                j = 1
                while j <= 2:
                    d.swipe_ext('up', scale=0.8)
                    time.sleep(2.0)
                    j += 1
                d.click(0.578, 0.236)
            else:
                d.swipe_ext(Direction.FORWARD, scale=0.9)

            # Tìm kiếm chủ đề và lướt xem
            # d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/nty"]/android.widget.ImageView[2]').click()
            # time.sleep(1)
            # for char in "Minrie Official":
            #     d.send_keys(char)
            #     time.sleep(random.uniform(0.08, 0.3))
            # print()
            # d(resourceId="com.ss.android.ugc.trill:id/odi").click()
            # d.swipe_ext(Direction.FORWARD, scale=1.0)
            # time.sleep(1.0)
            # d.swipe_ext(Direction.FORWARD, scale=1.0)

            # Xem live, lướt live và bình luận
            d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/nty"]/android.widget.ImageView[1]').click()
            time.sleep(15.0)
            d.swipe_ext(Direction.FORWARD)
            time.sleep(5.0)
            d.swipe_ext(Direction.FORWARD)
            d(resourceId="com.ss.android.ugc.trill:id/ebx").click()
            for char in "Nice bro!":
                d.send_keys(char)
                time.sleep(random.uniform(0.08, 0.3))
            print()
            d.press('enter')
            time.sleep(2.0)
            d(resourceId="com.ss.android.ugc.trill:id/cgv").click()

            # Vào cửa hàng
            d(text="Cửa hàng").click()
            for i in range(0, 2, 1):
                d.swipe_ext('up', scale=0.9)
                time.sleep(1)

            # thoát quảng cáo
            d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/fhp"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.LynxFlattenUI[17]').click()
            d(text="Hộp thư").click()



        except Exception as e:
            print(f"Lỗi khi chạy trên thiết bị {self.device}: {e}")

def main(m):
    device = devices_list[m]
    run = starts(device)
    run.start()  # Sửa lại từ run.run() thành run.start()

if __name__ == "__main__":
    for m in range(thread_count):
        main(m)