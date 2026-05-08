import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd
from gpiozero import Button

# Setup I2C and LCD
i2c = busio.I2C(board.SCL, board.SDA)
# 16 columns, 2 rows, address 0x27
lcd = character_lcd.Character_LCD_I2C(i2c, 16, 2, address=0x27)

button = Button(17)
counter = 0

while True:
    lcd.clear()
    
    if button.is_pressed:
        face = "NOM NOM NOM"
    elif counter == 0:
        face = "( ^_^ )"
    elif counter == 1:
        face = "( O_o )"
    elif counter == 2:
        face = "( -_- )"
    elif counter == 3:
        face = "( >_< )"
    else:
        face = "( -.- )zZ"

    # Send text to the LCD
    lcd.message = face

    if button.is_pressed == False:
        counter = counter + 1
        if counter > 4:
            counter = 0
            
    time.sleep(0.5)