import time
from RPLCD.i2c import CharLCD
from gpiozero import Button

# 1. Initialize the LCD and the Button
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)
button = Button(17)

# 2. Create a variable to keep track of which face to show
face_state = 1

# 3. Run the infinite loop
while True:
    lcd.clear()
    
    # Check the variable and print the matching face
    if face_state == 1:
        lcd.write_string("    ( ^_^ )     \r\n     Happy!     ")
    elif face_state == 2:
        lcd.write_string("    ( O_o )     \r\n      Huh?      ")
    elif face_state == 3:
        lcd.write_string("    ( -_- )     \r\n      Sigh      ")
    elif face_state == 4:
        lcd.write_string("    ( >_< )     \r\n     Yikes!     ")
    elif face_state == 5:
        lcd.write_string("   ( -.- )zZ    \r\n    Sleeping    ")
        
    # Wait for 2 seconds OR until the button is pressed
    was_pressed = button.wait_for_press(timeout=2)
    
    # If the button was pressed, feed the digital pet!
    if was_pressed:
        lcd.clear()
        lcd.write_string("   ( ^o^ )      \r\n   Nom Nom...   ")
        time.sleep(2)   # Leave the eating face on screen for 2 seconds
        face_state = 1  # Reset the state back to Happy after eating
        
    # If the button was NOT pressed, just advance the face normally
    else:
        face_state += 1
        
        # If we've gone past the 5th face, reset the variable back to 1
        if face_state > 5:
            face_state = 1