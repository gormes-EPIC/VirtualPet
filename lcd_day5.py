import time
from RPLCD.i2c import CharLCD
from gpiozero import Button

# 1. Initialize the LCD and the Button
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)
button = Button(17)

# 2. Setup our tracking variables
# time.time() gets the current time in seconds. We use this like a stopwatch.
last_feed_time = time.time() 

# We track the "mood" so we only update the screen when the mood actually changes.
# This prevents the LCD from constantly clearing and flickering!
current_mood = "" 

hunger = 50

# 3. Run the infinite loop
while True:
    
    # --- STATE 1: THE BUTTON IS PRESSED (FEEDING) ---
    if button.is_pressed:
        lcd.clear()
        lcd.write_string("   ( ^o^ )      \r\n   Nom Nom...   ")
        time.sleep(2)                 # Give the pet 2 seconds to eat
        
        last_feed_time = time.time()  # Reset our stopwatch!
        current_mood = "eating"       # Force the screen to update after eating
        hunger = 500

    # --- STATE 2: THE BUTTON IS NOT PRESSED ---
    else:
        # Calculate how many seconds have passed since the last meal
        seconds_idle = time.time() - last_feed_time
        
        hunger -= 1

        # If it has been more than 10 seconds -> Sleep
        if seconds_idle > 10:
            if current_mood != "sleeping":
                lcd.clear()
                lcd.write_string("   ( -.- )zZ    \r\n    Sleeping    ")
                current_mood = "sleeping" # Remember that we are now sleeping
                
        # If it has been less than 10 seconds -> Happy
        elif hunger <= 0:
            if current_mood != "hungry":
                lcd.clear()
                lcd.write_string("    ( O_o )     \r\n    Hungry!     ")
                current_mood = "hungry"    # Remember that we are now happy
    
        else:
            if current_mood != "happy":
                lcd.clear()
                lcd.write_string("    ( ^_^ )     \r\n     Happy!     ")
                current_mood = "happy"    # Remember that we are now happy
                
    # A tiny pause so the Raspberry Pi doesn't max out its processor
    # checking the button thousands of times a second
    time.sleep(0.1)