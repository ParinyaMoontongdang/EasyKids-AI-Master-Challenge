import sensor, image, time, math

# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
# The below thresholds track in general red/green things. You may wish to tune them...
thresholds = [(51, 72, 8, 53, -8, 19), # generic_red_thresholds -> index is 0 so code == (1 << 0)
              (30, 100, -64, -8, -32, 32)] # generic_green_thresholds -> index is 1 so code == (1 << 1)
# Codes are or'ed together when "merge=True" for "find_blobs".

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs(thresholds, pixels_threshold=100, area_threshold=5000, merge=True):

        print("blob.code = ",blob.code())

        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        # Note - the blob rotation is unique to 0-180 only.
        img.draw_keypoints([(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20)


        #if blob.code() == 3: # r/g code == (1 << 1) | (1 << 0)
            # These values depend on the blob not being circular - otherwise they will be shaky.
            # if blob.elongation() > 0.5:
            #     img.draw_edges(blob.min_corners(), color=(255,0,0))
            #     img.draw_line(blob.major_axis_line(), color=(0,255,0))
            #     img.draw_line(blob.minor_axis_line(), color=(0,0,255))
            # These values are stable all the time.

    #print(clock.fps())
