import uiautomator2 as u2
import random
import time

d = u2.connect('5200f86bea482501')

i = 0
while i <= 5:
    d.swipe_ext('up', scale=0.6)
    time.sleep(10.0)
    isLike = random.randint(0, 1)
    if isLike == 1:
        d(resourceId="com.ss.android.ugc.trill:id/deu").click()
    else:
        d(resourceId="com.ss.android.ugc.trill:id/cf4").click()
        time.sleep(3.0)
        j = 0
        while j < 2:
            d.swipe_ext('up', scale=0.8)
            time.sleep(3.0)
            j += 1
        d.click(0,0)
    i += 1
d(text="Hồ sơ").click()
time.sleep(1.0)
d.swipe_ext('up', scale=0.8)