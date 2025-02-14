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

def bypass_slide(devices):
    pipe = subprocess.Popen(f'adb -s {devices} exec-out screencap -p',
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, 
                        shell=True)
        #image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    image_bytes = pipe.stdout.read()
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    # img = image[430:765, 102:648] # cắt chỗ có captcha # cut zone captcha
    img = image[360:580, 100:440]
    # img = image[400:1505, 80:1248]
    #cv2.imshow("a", img)
    #cv2.waitKey(0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img3 = cv2.Canny(gray, 200, 200, L2gradient=True)
    kernel = np.ones([23,23]) # Tạo kernel
    kernel[2:,2:] = -0.1
    im = cv2.filter2D(img3/255, -1, kernel)
    im1 = im[:,:125]
    y1,x1 = np.argmax(im1)//im1.shape[1], np.argmax(im1)%im1.shape[1] # Tìm vị trí 1 chính xác
    im2 = im[:,125:]
    y2,x2 = np.argmax(im2)//im2.shape[1], np.argmax(im2)%im2.shape[1] + 125 # Tìm vị trí 1 chính xác
    # cv2.rectangle(img, (x1,y1), (x1+50, y1+50), 255, 2)
    # cv2.rectangle(img, (x2,y2), (x2+50, y2+50), 255, 2)
    # plt.imshow(img)
    # plt.show()
    return x2-x1


class Auto:
    def __init__(self, device_id):
        self.device = u2.connect(device_id)

    # Mở app
    def open_app(self):
        self.device(resourceId="com.sec.android.app.launcher:id/iconview_titleView", text="TikTok").click()

    # Đóng app
    def close_app(self):
        self.device.app_stop("com.ss.android.ugc.trill")

    # Lướt video
    def swipe_video(self, video: int):
        i = 1
        while i <= video:
            self.device.swipe_ext('up', scale=random.uniform(0.8, 1.0))
            time.sleep(random.randint(5, 15))
            if self.device(resourceId="com.ss.android.ugc.trill:id/deu").exists:
                self.device(resourceId="com.ss.android.ugc.trill:id/deu").click()
                time.sleep(random.randint(2, 5))
                self.device(resourceId="com.ss.android.ugc.trill:id/cf4").click()
                self.device.swipe_ext(Direction.FORWARD, scale=random.uniform(0.8, 1.0))
                time.sleep(2.0)
                self.device.swipe_ext(Direction.FORWARD, scale=random.uniform(0.8, 1.0))
                time.sleep(5.0)
                self.device.click(0.47, 0.178)
            else:
                self.device.swipe_ext('up', scale=random.uniform(0.8, 1.0))
                time.sleep(random.randint(5, 15))
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
        # self.device.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/mi7"]/android.widget.ImageView[1]').click()
        time.sleep(10.0)
        self.device.swipe_ext(Direction.FORWARD)
        time.sleep(random.randint(5, 15))
        self.device.swipe_ext(Direction.FORWARD)
        time.sleep(random.randint(5, 20))
        # Bình luận live
        self.device(resourceId="com.ss.android.ugc.trill:id/dx8").click()
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
        if self.device(resourceId="com.sec.android.app.launcher:id/clear_all_button").exists:
            self.device(resourceId="com.sec.android.app.launcher:id/clear_all_button").click()
        time.sleep(2.0)
        self.device.press('home')

    # Mở app check proxy
    def open_proxy_app(self):
        self.device.xpath('//*[@content-desc="Show My IP Address"]/android.widget.ImageView[1]').click()
        time.sleep(1.0)
        self.device(resourceId="com.titantech.showmyipaddress:id/btn_recheckip").click()

    # Trở về home
    def return_home(self):
        self.device.press('home')

    # Check pop-up window
    def check_window(self):
        if self.device(text="Allow access to phone data?").exists:
            return True
        return False
    
    # click OK
    def click(self):
        self.device(resourceId="android:id/button1").click()

    # Start session
    def init_session(self):
        self.device.session("com.ss.android.ugc.trill", attach=True)

    # Kiểm tra xem app đang chạy là gì?
    def check_current_app(self):
        print(f'{self.device} đang chạy {self.device.app_current()}')
        

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

            
            if d.check_window():
                d.click()
                time.sleep(10.0)
            
            # d.return_home()
            # time.sleep(1.0)
            # d.open_app()
            # time.sleep(15.0)
            # d.swipe_video(6)
            # d.check_current_app()

            def capcha(d3):
                poin = d3.find('img\\slide.png')
    
                if poin:  # Kiểm tra xem có tọa độ nào không
                    d3.slideCaptcha(poin[0][0], poin[0][1])
        
                time.sleep(2)

            capcha(d3)  # Gọi hàm

            
            # def min1(d):
            #     poin  = d.find('img\\1.png')
            #     if poin > [(0, 0)] :
            #         d.click(poin[0][0],poin[0][1])
            #         capcha(d)
            # min1(d)



        except Exception as e:
            print(f"Lỗi khi chạy trên thiết bị {self.device}: {e}")

def main(m):
    
    run = starts(devices_list[m])
    run.start()  # Sửa lại từ run.run() thành run.start()




class ADB:
    def __init__(self, handle):
        self.handle = handle

    def screen_capture(self):
        #os.system(f'adb -s {self.handle} exec-out screencap -p > {name}.png')
        pipe = subprocess.Popen(f'adb -s {self.handle} exec-out screencap -p',
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, shell=True)
        #image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
        image_bytes = pipe.stdout.read()
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
        return image

    def swipe(self, x1, y1, x2, y2):
        subprocess.call(f"adb -s {self.handle} shell input touchscreen swipe {x1} {y1} {x2} {y2} 1000", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def find(self,img='',threshold=0.99):
        img = cv2.imread(img) #sys.path[0]+"/"+img)
        img2 = self.screen_capture()    
        result = cv2.matchTemplate(img,img2,cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        retVal = list(zip(*loc[::-1]))
        #image = cv2.rectangle(img2, retVal[0],(retVal[0][0]+img.shape[0],retVal[0][1]+img.shape[1]), (0,250,0), 2)
        #cv2.imshow("test",image)
        #cv2.waitKey(0)
        #cv2.destroyWindow("test")
        return retVal

    def slideCaptcha(self,x,y):
        # adb.excuteAdb(sr, "adb shell screencap -p /sdcard/cap.png")
        # adb.excuteAdb(sr, f"adb pull /sdcard/cap.png {sr}/captcha.png")
        captcha = bypass_slide(self.handle)
        self.swipe(round(x), round(y), int(x)+int(captcha), round(y))
        return True

    # Restart wifi
    def restart_wifi(self):
        subprocess.run(f'adb -s {self.handle} shell svc wifi disable && adb -s {self.handle} shell svc wifi enable', shell=True, check=True)
        print(f'{self.handle} restart wifi succeed!')

    def chage_rotation(self):
        subprocess.call(f'adb -s {self.handle} shell settings put system user_rotation 0')
        print(f'Device {self.handle} change rotation succeed')
    
    # Đổi proxy
    def changeProxy(self, ip):
        """
        Input Proxy Http IP:PORT
        Thêm Proxy Http IP:PORT
        """
        subprocess.call(f'adb -s {self.handle} shell settings put global http_proxy {ip}', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # Xóa proxy
    def remProxy(self):
        """
        Input Proxy Http IP:PORT
        Thêm Proxy Http IP:PORT
        """
        subprocess.call(f'adb -s {self.handle} shell settings put global http_proxy :0', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(f'{self.handle} remove proxy succeed')

    # Kiểm tra proxy
    def get_proxy(self):
        proxy = subprocess.check_output(f"adb -s {self.handle} shell settings get global http_proxy", shell=True).decode().strip()
        print(f'{self.handle} có proxy: {proxy if proxy else "Không có proxy"}')

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