import time
import board
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# 1. Setup the LCD dimensions
lcd_columns = 16
lcd_rows = 2

# 2. Initialize the I2C bus and the LCD
i2c = board.I2C()
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

# 3. Run the infinite loop with sequential commands
while True:
    # Face 1
    lcd.clear()
    lcd.message = "    ( ^_^ )     \n     Happy!     "
    time.sleep(2)
    
    # Face 2
    lcd.clear()
    lcd.message = "    ( O_o )     \n      Huh?      "
    time.sleep(2)
    
    # Face 3
    lcd.clear()
    lcd.message = "    ( -_- )     \n      Sigh      "
    time.sleep(2)
    
    # Face 4
    lcd.clear()
    lcd.message = "    ( >_< )     \n     Yikes!     "
    time.sleep(2)
    
    # Face 5
    lcd.clear()
    lcd.message = "   ( -.- )zZ    \n    Sleeping    "
    time.sleep(2)