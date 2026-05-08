import time
from RPLCD.i2c import CharLCD

# Initialize the LCD (Update address to 0x3F if 0x27 doesn't work)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)

# The list of faces to cycle through
faces = [
    "( ^_^ )", 
    "( O_o )", 
    "( -_- )", 
    "( >_< )", 
    "( -.- )zZ"
]

print("Cycling LCD faces... Press Ctrl+C to stop.")

try:
    while True:
        for face in faces:
            lcd.clear() # Wipe the screen clean
            
            # Math to center the face on the 16-character width
            padding = (16 - len(face)) // 2 
            
            # Move cursor to Row 0 (top line), Column [padding]
            lcd.cursor_pos = (0, padding)
            lcd.write_string(face)
            
            time.sleep(2)

except KeyboardInterrupt:
    # Safely clear and close the display when you exit
    lcd.clear()
    lcd.close(clear=True)
    print("\nDone.")