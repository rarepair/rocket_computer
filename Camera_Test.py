import time
from datetime import datetime
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from libcamera import controls
from pathlib import Path

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

picam2.set_controls({"FrameRate": 60})

encoder = H264Encoder(10000000)

now = datetime.now()
current_time = now.strftime("%H_%M_%S_%f")
text_filename = Path("~/flightdata/Camera_Data_" + current_time + ".h264").expanduser()

time.sleep(5) # plus 5

picam2.start_recording(encoder, str(text_filename))
time.sleep(1800)
picam2.stop_recording()
