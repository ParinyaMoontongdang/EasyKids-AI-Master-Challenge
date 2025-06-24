import sensor, image, time, lcd
from maix import KPU
import gc

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 1000)
clock = time.clock()

IMG_SIZE = 224

obj_name = ('mechanic', 'musician', 'barista')
anchor = (2.34, 5.41, 2.16, 4.58, 2.66, 5.97, 2.98, 5.81, 1.78, 4.62)
kpu = KPU()
kpu.load_kmodel("/sd/art_toy.kmodel")
kpu.init_yolo2(anchor, anchor_num=(int)(len(anchor)/2), img_w=IMG_SIZE, img_h=IMG_SIZE,
               net_w=IMG_SIZE, net_h=IMG_SIZE, layer_w=7, layer_h=7,
               threshold=0.5, nms_value=0.2, classes=len(obj_name))

try:
    while True:
        clock.tick()
        img = sensor.snapshot()
        resized = img.resize(IMG_SIZE, IMG_SIZE)
        resized.pix_to_ai()

        kpu.run_with_output(resized)
        dect = kpu.regionlayer_yolo2()
        if len(dect) > 0:
            for l in dect:
                scale_x = 320 / IMG_SIZE
                scale_y = 240 / IMG_SIZE

                x = int(l[0] * scale_x)
                y = int(l[1] * scale_y)
                w = int(l[2] * scale_x)
                h = int(l[3] * scale_y)

                img.draw_rectangle(x, y, w, h, color=(0, 255, 0))
                img.draw_string(x, y - 10, obj_name[l[4]], color=(255, 0, 0), scale=1.5)
                print("Detected:", obj_name[l[4]])

        lcd.display(img)
        gc.collect()

except Exception as e:
    print("Error:", e)

finally:
    kpu.deinit()
