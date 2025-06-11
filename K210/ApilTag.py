import sensor, image, time, lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
lcd.init()

while(True):
    img = sensor.snapshot()
    tag = img.find_apriltags()
    
    if len(tag) > 0:
        img.draw_string(7,8, str(tag[0].id()), color=(0,128,0), scale=4)
        img.draw_rectangle(tag[0].x(), tag[0].y(),tag[0].w(),tag[0].h(),color=(255,0,0),thickness=3)
        print(tag[0].id())
        
    lcd.display(img)
