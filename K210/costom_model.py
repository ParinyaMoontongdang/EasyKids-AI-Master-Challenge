import sensor, image, time, lcd
from maix import KPU
import gc

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)   # 320x240
sensor.skip_frames(time = 1000)
clock = time.clock()

# ใช้ขนาดตรงกับตอนเทรน
IMG_SIZE = 224

# โหลดโมเดล
obj_name = ("stop", "right", "model")
anchor = (1.92,1.97,1.56,1.55,1.23,1.28,1.81,2.97,2.19,2.27)
kpu = KPU()
print("ready load model")
kpu.load_kmodel("/sd/test_model.kmodel")
kpu.init_yolo2(anchor, anchor_num=5, img_w=IMG_SIZE, img_h=IMG_SIZE,
               net_w=IMG_SIZE, net_h=IMG_SIZE, layer_w=7, layer_h=7,
               threshold=0.5, nms_value=0.2, classes=3)

# ลูปหลัก
try:
    while True:
        clock.tick()
        img = sensor.snapshot()
        resized = img.resize(IMG_SIZE, IMG_SIZE)
        resized.pix_to_ai()

        kpu.run_with_output(resized)
        dect = kpu.regionlayer_yolo2()

        # แสดงผล
        if len(dect) > 0:
            for l in dect:
                # ปรับตำแหน่งสัดส่วนกลับมาที่หน้าจอ 320x240
                scale_x = 320 / IMG_SIZE
                scale_y = 240 / IMG_SIZE

                x = int(l[0] * scale_x)
                y = int(l[1] * scale_y)
                w = int(l[2] * scale_x)
                h = int(l[3] * scale_y)

                img.draw_rectangle(x, y, w, h, color=(0, 255, 0))
                img.draw_string(x, y - 10, obj_name[l[4]], color=(255, 0, 0), scale=1.5)
                print("Detected:", obj_name[l[4]])

        img.draw_string(0, 0, "%2.1f fps" % clock.fps(), color=(0, 60, 128), scale=1.0)
        lcd.display(img)
        gc.collect()

except Exception as e:
    print("Error:", e)

finally:
    kpu.deinit()
