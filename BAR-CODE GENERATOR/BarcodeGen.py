# BAR-CODE GENERATOR
import os
import qrcode as qr

path = os.path.dirname(os.path.abspath(__file__))       
img = qr.make("https://github.com/Shikher-jain/SJ_MAIN")  # jo bhi chaoye uska text ya url
img.save(path"/SJ_GitHub.png")

