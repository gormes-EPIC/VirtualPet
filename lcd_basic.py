import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Setup I2C and LCD (16 columns, 2 rows, address 0x27)
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_I2C(i2c, 16, 2, address=0x27)

counter = 0

while True:
    # Clear the screen for the new face
    lcd.clear()
    
    # Logic to pick the face based on the counter
    if counter == 0:
        face = "( ^_^ )"
    elif counter == 1:
        face = "( O_o )"
    elif counter == 2:
        face = "( -_- )"
    elif counter == 3:
        face = "( >_< )"
    else:
        face = "( -.- )zZ"

    # Display the face
    lcd.message = face

    # Increment counter and reset if it hits the end
    counter = counter + 1
    if counter > 4:
        counter = 0
            
    # Wait 2 seconds before the next face
    time.sleep(2)