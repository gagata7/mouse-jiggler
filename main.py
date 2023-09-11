import usb_hid
from lib.adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)
while True:
    m.move(-1, 0)
    m.move(1,0)