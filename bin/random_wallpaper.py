import random
import os

os.chdir("/home/user/Images/walpapers")
l = os.listdir(".")
os.system(f"feh --no-fehbg --bg-fill /home/user/Images/walpapers/{l[random.randint(0, len(l)-1)]} /home/user/Images/walpapers/wallhaven-1peepw.png")
