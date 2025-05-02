import time
import board
import busio
from adafruit_bno08x import (
    BNO_REPORT_ACCELEROMETER,
    BNO_REPORT_GYROSCOPE,
    BNO_REPORT_MAGNETOMETER,
    BNO_REPORT_ROTATION_VECTOR,
)
from adafruit_bno08x.i2c import BNO08X_I2C
from adafruit_extended_bus import ExtendedI2C as I2C
from datetime import datetime
from time import sleep
from pathlib import Path

bno = BNO08X_I2C(I2C(3))

bno.enable_feature(BNO_REPORT_ACCELEROMETER)
bno.enable_feature(BNO_REPORT_GYROSCOPE)
bno.enable_feature(BNO_REPORT_MAGNETOMETER)
bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)

now = datetime.now()
current_time = now.strftime("%H_%M_%S_%f")
text_filename = Path("~/flightdata/IMU_Data_" + current_time + ".txt").expanduser()

print("Collecting Data...")

with open(text_filename, "w") as f:

    while True:
        accel_x, accel_y, accel_z = bno.acceleration  # pylint:disable=no-member
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S_%f")
        f.write(current_time + " - Acc: X: %0.6f  Y: %0.6f Z: %0.6f  m/s^2" % (accel_x, accel_y, accel_z))
        f.write("\n")


        gyro_x, gyro_y, gyro_z = bno.gyro  # pylint:disable=no-member
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S_%f")
        f.write(current_time + " - Gyro: X: %0.6f  Y: %0.6f Z: %0.6f rads/s" % (gyro_x, gyro_y, gyro_z))
        f.write("\n")


        mag_x, mag_y, mag_z = bno.magnetic  # pylint:disable=no-member
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S_%f")
        f.write(current_time + " - Magno: X: %0.6f  Y: %0.6f Z: %0.6f uT" % (mag_x, mag_y, mag_z))
        f.write("\n")


        quat_i, quat_j, quat_k, quat_real = bno.quaternion  # pylint:disable=no-member
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S_%f")
        f.write(current_time + " - Quat I: %0.6f  J: %0.6f K: %0.6f  Real: %0.6f" % (quat_i, quat_j, quat_k, quat_real))
        f.write("\n")
        sleep(0.02)

