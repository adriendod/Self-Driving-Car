from camera import Camera
import pandas as pd

df = pd.DataFrame()
driving_direction = -1

cam = Camera()
cam.capture_frame()
cam.save_frame(df, driving_direction, "/")