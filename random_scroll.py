import uiautomator2 as u2
import random
import time

d = u2.connect('5200f86bea482501')
i=0
while i<10:
    d.swipe_ext('up', scale=random.random())
    time.sleep(2)
    i+=1