import sensor, image, lcd, os, time
from modules import ybkey

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames(time=2000)

KEY = ybkey()

img_count = 0

while True:
    img = sensor.snapshot()
    resized = img.resize(224,224)
    if KEY.is_press():
        print("Button Pressed!")
        filename = "/sd/image_%03d.jpg" % img_count

        try:
            resized.save(filename)
            msg = "Saved: image_%03d.jpg" % img_count
            lcd.display(resized)
            lcd.draw_string(10, 220, msg, lcd.BLACK, lcd.GREEN)
            print(msg)
            img_count += 1
        except Exception as e:
            lcd.draw_string(10, 220, "Save failed!", lcd.RED, lcd.BLACK)
            print("Save failed:", e)

        time.sleep_ms(100)
        
    else:
        lcd.display(resized)
