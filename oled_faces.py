import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Initialize I2C and the OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Load the default system font
font = ImageFont.load_default()

# The list of faces to cycle through
faces = [
    "( ^_^ )", 
    "( O_o )", 
    "( -_- )", 
    "( >_< )", 
    "( -.- )zZ"
]

print("Cycling OLED faces... Press Ctrl+C to stop.")

try:
    while True:
        for face in faces:
            # 1. Create a blank black canvas matching the screen size
            image = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(image)
            
            # 2. Draw the text onto that canvas using X/Y coordinates
            # X=35, Y=25 roughly centers it on a 128x64 screen
            draw.text((35, 25), face, font=font, fill=255)
            
            # 3. Push the canvas to the OLED and display it
            oled.image(image)
            oled.show()
            
            time.sleep(2)

except KeyboardInterrupt:
    # Fill the screen with black (0) and show it to clear it
    oled.fill(0)
    oled.show()
    print("\nDone.")