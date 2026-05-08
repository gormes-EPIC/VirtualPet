import time
from RPLCD.i2c import CharLCD
from gpiozero import Button

# 1. Initialize the LCD and Button
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)
button = Button(17)

# 2. Run the game loop
while True:
    # Step A: Give the instruction
    lcd.clear()
    lcd.write_string("Press the button\r\n   Waiting...   ")
    
    # Step B: Pause the ENTIRE program until the physical button is pressed
    button.wait_for_press()
    
    # Step C: The reaction! 
    # This only runs AFTER the button is pressed
    lcd.clear()
    lcd.write_string("    BOOM!!!     \r\n   Great job!   ")
    
    # Wait 3 seconds so they can read the success message before it restarts
    time.sleep(3)