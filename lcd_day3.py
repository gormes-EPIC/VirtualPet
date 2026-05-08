import time
from RPLCD.i2c import CharLCD

# 1. Initialize the LCD
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

# 2. Create a variable to keep track of the current face
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
        
    # Wait for 2 seconds so the face can be seen
    time.sleep(2)
    
    # Add 1 to the variable to move to the next face for the next loop
    face_state += 1
    
    # Reset back to 1 if we pass the 5th face
    if face_state > 5:
        face_state = 1