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

    # Mở app
    def open_app(self):
        self.device.app_start("com.ss.android.ugc.trill")

    # Đóng app
    def close_app(self):
        self.device.app_stop("com.ss.android.ugc.trill")

    # Lướt video
    def swipe_video(self, video: int):
        i = 1
        while i <= video:
            self.device.swipe_ext('up', scale=random.uniform(0.8, 1.0))
            time.sleep(random.randint(5, 10))
            if self.device(resourceId="com.ss.android.ugc.trill:id/dt4").exists:
                self.device(resourceId="com.ss.android.ugc.trill:id/dt4").click()
                time.sleep(random.randint(2, 5))
                self.device(resourceId="com.ss.android.ugc.trill:id/cos").click()
                self.device.swipe_ext(Direction.FORWARD, scale=random.uniform(0.8, 1.0))
                time.sleep(2.0)
                self.device.swipe_ext(Direction.FORWARD, scale=random.uniform(0.8, 1.0))
                time.sleep(5.0)
                self.device.click(0.47, 0.178)
            else:
                self.device.swipe_ext('up', scale=random.uniform(0.8, 1.0))
                time.sleep(8.0)
            i += 1

    # Tìm kiếm chủ đề theo từ khóa
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

    # Xem live
    def watch_live(self):
        self.device.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/nty"]/android.widget.ImageView[1]').click()
        time.sleep(5.0)
        self.device.swipe_ext(Direction.FORWARD)
        time.sleep(5.0)
        self.device.swipe_ext(Direction.FORWARD)
        time.sleep(5.0)
        # Bình luận live
        self.device(resourceId="com.ss.android.ugc.trill:id/ebx").click()
        time.sleep(2.0)
        for char in "Nice bro":
            self.device._send_keys_with_ime(char)
            time.sleep(random.uniform(0.08, 0.3))
        self.device.press('enter')

    # Vào xem giỏ hàng
    def click_store(self, watch: int):
        self.device(text="Cửa hàng").click()
        time.sleep(9.0)
        while self.device.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/fhp"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.component.svg.UISvg[1]').exists:
            self.device.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/fhp"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.component.svg.UISvg[1]').click()
        i = 1
        while i <= watch:
            self.device.swipe_ext(Direction.FORWARD, scale=random.uniform(0.7, 1.0))
            time.sleep(random.randint(2, 5))
            i += 1

    # Vào trang cá nhân
    def click_profile(self):
        # self.device(text="Hồ sơ").click()
        # time.sleep(5.0)
        # self.device.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/kh_"]/android.widget.ImageView[2]').click()
        # time.sleep(1.0)
        # self.device(resourceId="com.ss.android.ugc.trill:id/uy", text="Cài đặt và quyền riêng tư").click()
        # self.device.swipe(500, 1500, 500, 500, duration=1)
        # self.device(text="Ngôn ngữ").click()
        # self.device(text="Ngôn ngữ ứng dụng").click()
        # self.device.swipe_ext('up', scale=0.9)
        # self.device(resourceId="com.ss.android.ugc.trill:id/r0s", text="Tiếng Việt").click()
        self.device(resourceId="com.ss.android.ugc.trill:id/kh_").click()

    # Đóng tất cả app chạy ngầm
    def close_recent_apps(self):
        self.device.press('recent')
        if self.device(resourceId="com.miui.home:id/clearAnimView").exists:
            self.device(resourceId="com.miui.home:id/clearAnimView").click()
        time.sleep(1.0)
        self.device.press('home')
        

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

        try:
            d = Auto(self.device)
            d3 = ADB(self.device)
            if not d.device.info:
                print(f"Thiết bị {self.device} không sẵn sàng.")
                return

            d.swipe_video(5)
            



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