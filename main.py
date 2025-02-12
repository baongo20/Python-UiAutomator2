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
from  xml.dom.minidom import parse

try:
    import uiautomator2 as u2
except:
    os.system("pip install uiautomator2")
import uiautomator2 as u2
from uiautomator2 import Direction


class Auto:
    def __init__(self, device_id):
        self.device = u2.connect(device_id)
        # print(f"Đã kết nối với thiết bị: {self.device.info['serial']}")

    def open_app(self):
        self.device.click(0.148, 0.141)

    def close_app(self):
        self.device.app_stop("com.ss.android.ugc.trill")

    # Lướt video
    def swipe_video(self, video: int):
        i = 1
        while i <= video:
            time.sleep(8.0)
            self.device.swipe_ext('up', scale=random.uniform(0.8, 1.0))
            time.sleep(random.randint(5, 10))
            if self.device(resourceId="com.ss.android.ugc.trill:id/deu").exists():
                self.device(resourceId="com.ss.android.ugc.trill:id/deu").click()
                time.sleep(random.randint(2, 5))
                self.device(resourceId="com.ss.android.ugc.trill:id/cf4").click()
                self.device.swipe_ext(Direction.FORWARD, scale=random.uniform(0.8, 1.0))
                self.device.swipe_ext(Direction.FORWARD, scale=random.uniform(0.8, 1.0))
                time.sleep(5.0)
                self.device.click(0.47, 0.178)
            else:
                self.device.swipe_ext('up', scale=random.uniform(0.8, 1.0))
            i += 1

    # Tìm kiếm chủ đề theo từ khỏa
    def find_key_word(self, text: str):
        # self.device.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/mi7"]/android.widget.ImageView[2]').click()
        self.device.click(0.941, 0.058)
        for char in text:
            time.sleep(1.5)
            self.device.send_keys(char)
            time.sleep(random.uniform(0.08, 0.3))
        time.sleep(5.0)
        self.device.click(0.907, 0.049)

    # Trở về
    def back(self):
        self.device.press('back')

    # Tiếp tục tìm kiếm và lướt video
    def keep_find_key_word(self, text: str):
        for char in text:
            time.sleep(1.0)
            self.device.send_keys(char)
            time.sleep(random.uniform(0.08, 0.3))
        time.sleep(5.0)
        self.device.click(0.907, 0.049)
        time.sleep(3.0)
        self.device.swipe_ext(Direction.FORWARD, scale=random.uniform(0.8, 1.0))
        self.device.swipe_ext(Direction.FORWARD, scale=random.uniform(0.8, 1.0))
        

def get_devices():
    devices = subprocess.check_output("adb devices")
    p = str(devices).replace("b'List of devices attached","").replace('\\r\\n',"").replace(" ","").replace("'","").replace('b*daemonnotrunning.startingitnowonport5037**daemonstartedsuccessfully*Listofdevicesattached',"")
    if int(len(p)) > 0:
        listDevices = p.split("\\tdevice")
        listDevices.pop()
        return listDevices
    else:
        return 

devices_list = get_devices()
thread_count = len(devices_list)



class starts(threading.Thread):
    def __init__(self, device):
        super().__init__()
        self.device = device
       
    def run(self):
        # print(f"Khởi chạy cho thiết bị: {self.device}")
        try:
            d = Auto(self.device)
            d3 = ADB(self.device)
            if not d.device.info:
                print(f"Thiết bị {self.device} không sẵn sàng.")
                return
            
            
            # d.find_key_word("Minrie Official")
            # d.back()
            d.keep_find_key_word("make up")

            
            
            

            # # swipe 10 videos
            # i = 1
            # while i <= 4:
            #     d.swipe_ext('up', scale=random.uniform(0.8, 1.0))
            #     time.sleep(random.randint(5, 10))
            #     i += 1

            # # likes video và xem bình luận
            # if d(resourceId="com.ss.android.ugc.trill:id/dt4").exists():
            #     d(resourceId="com.ss.android.ugc.trill:id/dt4").click()
            #     time.sleep(5.0)
            #     d(resourceId="com.ss.android.ugc.trill:id/cos").click()
            #     j = 1
            #     while j <= 2:
            #         d.swipe_ext('up', scale=0.8)
            #         time.sleep(2.0)
            #         j += 1
            #     d.click(0.578, 0.236)
            # else:
            #     d.swipe_ext(Direction.FORWARD, scale=0.9)

            # # Tìm kiếm chủ đề và lướt xem
            # # d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/nty"]/android.widget.ImageView[2]').click()
            # # time.sleep(1)
            # # for char in "Minrie Official":
            # #     d.send_keys(char)
            # #     time.sleep(random.uniform(0.08, 0.3))
            # # print()
            # # d(resourceId="com.ss.android.ugc.trill:id/odi").click()
            # # d.swipe_ext(Direction.FORWARD, scale=1.0)
            # # time.sleep(1.0)
            # # d.swipe_ext(Direction.FORWARD, scale=1.0)

            # # Xem live, lướt live và bình luận
            # d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/nty"]/android.widget.ImageView[1]').click()
            # time.sleep(15.0)
            # d.swipe_ext(Direction.FORWARD)
            # time.sleep(5.0)
            # d.swipe_ext(Direction.FORWARD)
            # d(resourceId="com.ss.android.ugc.trill:id/ebx").click()
            # for char in "Nice bro!":
            #     d.send_keys(char)
            #     time.sleep(random.uniform(0.08, 0.3))
            # print()
            # d.press('enter')
            # time.sleep(2.0)
            # d(resourceId="com.ss.android.ugc.trill:id/cgv").click()

            # # Vào cửa hàng
            # d(text="Cửa hàng").click()
            # for i in range(0, 2, 1):
            #     d.swipe_ext('up', scale=0.9)
            #     time.sleep(1)

            # # thoát quảng cáo
            # d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/fhp"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.LynxFlattenUI[17]').click()
            # d(text="Hộp thư").click()



        except Exception as e:
            print(f"Lỗi khi chạy trên thiết bị {self.device}: {e}")

def main(m):
    
    run = starts(devices_list[m])
    run.start()  # Sửa lại từ run.run() thành run.start()




class ADB:
    def __init__(self, handle):
        self.handle = handle

    def chage_rotation(self):
        subprocess.call(f'adb -s {self.handle} shell settings put system user_rotation 0')
        print(f'Device {self.handle} change rotation succeed')
    
    def changeProxy(self, ip):
        """
        Input Proxy Http IP:PORT
        Thêm Proxy Http IP:PORT
        """
        subprocess.call(f'adb -s {self.handle} shell settings put global http_proxy {ip}', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def remProxy(self):
        """
        Input Proxy Http IP:PORT
        Thêm Proxy Http IP:PORT
        """
        subprocess.call(f'adb -s {self.handle} shell settings put global http_proxy :0', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        # print(f'{self.handle} remove proxy succeed')

    def get_proxy(self):
        proxy = subprocess.check_output("adb shell settings get global http_proxy")
        print(f'{self.handle} có {proxy}')

def assign_proxies(proxy_file):
    """
    Đọc danh sách proxy từ tệp và gán proxy cho từng thiết bị.
    """
    if not devices_list:
        print("Không có thiết bị nào được kết nối.")
        return
    
    try:
        with open(proxy_file, "r") as f:
            proxies = [line.strip() for line in f.readlines() if line.strip()]
        
        if len(proxies) < len(devices_list):
            print("Cảnh báo: Số lượng proxy ít hơn số lượng thiết bị. Một số thiết bị sẽ không có proxy.")
        
        for i, device in enumerate(devices_list):
            if i < len(proxies):
                proxy = proxies[i]
                adb = ADB(device)
                adb.changeProxy(proxy)
                print(f"Đã gán proxy {proxy} cho thiết bị {device}")
            else:
                print(f"Không đủ proxy cho thiết bị {device}, bỏ qua.")
    
    except Exception as e:
        print(f"Lỗi khi gán proxy: {e}")

if __name__ == "__main__":
    # Đọc proxy từ file và gán cho từng thiết bị trước khi chạy
    # assign_proxies("proxy.txt")
    
    for m in range(thread_count):
        main(m)