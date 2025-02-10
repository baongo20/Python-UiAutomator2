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
                d(text="TikTok").click()
            except Exception as e:
                print(f"Lỗi khi kết nối thiết bị {device}: {e}")
        batdau(device)

def main():
    # device = devices_list[m]
    run = starts("52000a83c0eb543f")
    run.start()  # Sửa lại từ run.run() thành run.start()

# threads = []

# for m in range(thread_count):
#     t = threading.Thread(target=main, args=(m,))
#     t.start()
#     threads.append(t)

# # Đợi tất cả luồng hoàn thành
# for t in threads:
#     t.join()

# def run_device(device):
#     try:
#         print(f"Đang kết nối đến {device}...")
#         d2 = Auto(device)
#         d = u2.connect(device)

#         if not d.info:
#             print(f"Thiết bị {device} không sẵn sàng.")
#             return
        
#         print(f"Mở TikTok trên {device}...")
#         # subprocess.Popen(f"adb -s {device} shell monkey -p com.zhiliaoapp.musically -c android.intent.category.LAUNCHER 1", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
#         d(text="TikTok").click()

#     except Exception as e:
#         print(f"Lỗi trên thiết bị {device}: {e}")

# if __name__ == "__main__":
#     devices_list = get_devices()

#     with concurrent.futures.ThreadPoolExecutor(max_workers=len(devices_list)) as executor:
#         executor.map(run_device, devices_list)

# class DeviceThread(threading.Thread):
#     def __init__(self, device_queue, resource_release_callback):
#         super().__init__()
#         self.device_queue = device_queue
#         self.resource_release_callback = resource_release_callback
#         self.device = None

#     def run(self):
#         while True:
#             try:
#                 self.device = self.device_queue.get(timeout=1)
#                 self.run_device_logic(self.device)
#             except queue.Empty:
#                 break # No more devices to process
#             except Exception as e:
#                 print(f"Error processing device {self.device}: {e}")
#             finally:
#                 if self.device:
#                     self.resource_release_callback(self.device) # Release the device back
#                     self.device_queue.task_done() # Mark the task complete

#     def run_device_logic(self, device):
#         try:
#             print(f"Đang kết nối đến {device}...")
#             d2 = Auto(device)
#             d = u2.connect(device)

#             if not d.info:
#                 print(f"Thiết bị {device} không sẵn sàng.")
#                 return

#             print(f"Mở TikTok trên {device}...")
#             d(text="TikTok").click()

#         except Exception as e:
#             print(f"Lỗi trên thiết bị {device}: {e}")


# def resource_release_callback(device):
#     """Callback function to release the device (resource)."""
#     with device_lock:
#         available_devices.append(device)
#         print(f"Device {device} trả về.")
#     device_available.release()


# def get_device():
#     """Get a device from the available list."""
#     device_available.acquire()  # Wait for a device to become available
#     with device_lock:
#         device = available_devices.pop(0)
#         print(f"Device {device} được cấp phát")
#         return device

# def main():
#     global available_devices, device_lock, device_available

#     devices_list = get_devices()
#     num_devices = len(devices_list)

#     # Initialize resources (devices)
#     available_devices = devices_list.copy()
#     device_lock = threading.Lock()
#     device_available = threading.Semaphore(num_devices)

#     # Initialize the task queue with devices.  Each device is a task.
#     device_queue = queue.Queue()
#     for device in devices_list:
#         device_queue.put(device)

#     threads = []
#     num_threads = min(num_devices, 5) # You can limit number of threads if needed
#     for _ in range(num_threads):
#         thread = DeviceThread(device_queue, resource_release_callback)
#         threads.append(thread)
#         thread.start()

#     device_queue.join()  # Wait for all devices to be processed
#     for thread in threads:
#         thread.join()  # Wait for all threads to complete

#     print("All devices processed.")


# if __name__ == "__main__":
#     main()