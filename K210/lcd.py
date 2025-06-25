import lcd

lcd.init()
lcd.clear(lcd.WHITE)

while(True):
    ## lcd.draw_string(x, y, text, text_color, bg_color) ##
    lcd.draw_string(10, 220, "Hello World!", lcd.BLACK, lcd.GREEN)
