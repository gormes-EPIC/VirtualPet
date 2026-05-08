import time
from RPLCD.i2c import CharLCD

# 1. Initialize the LCD
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

# 2. Start the infinite loop
while True:
    # Frame 1: Eyes Open
    lcd.clear()
    lcd.write_string("    ( O_O )     \r\n     Awake      ")
    time.sleep(1) # Pause for 1 second
    
    # Frame 2: Eyes Closed (Blinking)
    lcd.clear()
    lcd.write_string("    ( -_- )     \r\n     Blink      ")
    time.sleep(1) # Pause for 1 second