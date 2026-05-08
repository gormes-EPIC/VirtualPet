import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
font = ImageFont.load_default()

# Use a counter to track which face to show
counter = 0

while True:
    # Create the blank canvas
    image = Image.new("1", (128, 64))
    draw = ImageDraw.Draw(image)

    # Determine the text based on the counter value
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

    # Draw the face and update the screen
    draw.text((35, 25), face, font=font, fill=255)
    oled.image(image)
    oled.show()

    # Increase counter and reset it if it goes past 4
    counter = counter + 1
    if counter > 4:
        counter = 0

    time.sleep(2)