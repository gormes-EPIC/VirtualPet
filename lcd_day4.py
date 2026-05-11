import time
from RPLCD.i2c import CharLCD
from gpiozero import Button

# 1. Initialize the LCD and Button
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)
button = Button(17)

# 2. Run the game loop
while True:

    # If the button is pressed, then we can clear the screen and display our message
    if button.is_pressed:
        lcd.clear()
        lcd.write_string("    BOOM!!!     \r\n   Great job!   ")
    # If the button is not pressed, then we wait
    else: 
        lcd.clear()
        lcd.write_string("Press the button\r\n   Waiting...   ")
    
    
    # Wait 3 seconds so they can read the success message before it restarts
    time.sleep(3)