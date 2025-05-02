import time
import board
import adafruit_bmp3xx
from datetime import datetime
from pathlib import Path

i2c = board.I2C()
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2

now = datetime.now()
current_time = now.strftime("%H_%M_%S_%f")
text_filename = Path("~/flightdata/Alt_Data_" + current_time + ".txt").expanduser()

time.sleep(5) # plus 5

print("Collecting Data...")

with open(text_filename, "w") as f:

    while True:
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S_%f")
        f.write("T: {} P: {:6.4f} T: {:5.2f}".format(current_time, bmp.pressure, bmp.temperature))
        f.write("\n")
        #time.sleep(1)
