import sensor, image, time, math, lcd

thresholds = (51, 72, 8, 53, -8, 19) # generic_red_thresholds -> index is 0 so code == (1 << 0)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
lcd.init() 

while(True):
    img = sensor.snapshot()
    for blob in img.find_blobs(thresholds, pixels_threshold=100, area_threshold=100, merge=True):
        print("blob.code = ",blob.code())
        if blob.code() == 1: 
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
            img.draw_keypoints([(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20)
    lcd.display(img)
