import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Initialize I2C and the OLED
# On Pi 5, board.SCL and board.SDA usually map to I2C bus 1
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
except ValueError as e:
    print(f"I2C Initialization failed: {e}")
    print("Tip: Make sure I2C is enabled in sudo raspi-config")
    exit()

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

print("Cycling OLED faces on Pi 5... Press Ctrl+C to stop.")

try:
    while True:
        for face in faces:
            # 1. Create a blank black canvas (mode '1' for 1-bit color)
            image = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(image)
            
            # 2. Draw the text
            # We use draw.textbbox to help with centering dynamically
            bbox = draw.textbbox((0, 0), face, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (oled.width - text_width) // 2
            y = (oled.height - text_height) // 2
            
            draw.text((x, y), face, font=font, fill=255)
            
            # 3. Push to OLED
            oled.image(image)
            oled.show()
            
            time.sleep(2)

except KeyboardInterrupt:
    # Clear the screen on exit
    oled.fill(0)
    oled.show()
    print("\nDone.")