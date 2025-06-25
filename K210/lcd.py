import  lcd

lcd.init()

while(True):
    lcd.draw_string(10, 220, "Hello World!", lcd.BLACK, lcd.GREEN)
