from RPLCD.i2c import CharLCD

# 1. Initialize the LCD (specify chip, address, columns, and rows)
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

# 2. Clear the screen just in case there is old text left over
lcd.clear()

# 3. Print the nameplate
# The \r\n acts like hitting the "Enter" key to drop to the bottom row
lcd.write_string("   Jane Doe     \r\n Loves Python!  ")