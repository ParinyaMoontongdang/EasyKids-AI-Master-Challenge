import sensor, image, time, lcd

sensor.reset(dual_buff = True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
lcd.init()

# <---- tag_families ---->
#       image.TAG16H5 ## For EasyKids Ai Car ##
#       image.TAG25H7 
#       image.TAG25H9 
#       image.TAG36H10 
#       image.TAG36H11 
#       image.ARTOOLKIT

while(True):
    img = sensor.snapshot()
    tag = img.find_apriltags(families=image.TAG16H5)
    
    if len(tag) > 0:
        img.draw_rectangle(tag[0].rect(), color = (255, 0, 0),thickness=3)
        img.draw_string(7,8, str(tag[0].id()), color=(0,128,0), scale=3)
        
        resized = img.resize(320,240)
        resized.clear()
        resized.draw_string(120,60, str(tag[0].id()), color=(0,128,0), scale=10)
        print("Tag ID:", tag[0].id())
        lcd.display(resized)