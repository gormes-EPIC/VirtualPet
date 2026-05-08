import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
from gpiozero import Button

# Setup OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x27)
font = ImageFont.load_default()

# Setup Button on GPIO 17
button = Button(17)

counter = 0

while True:
    image = Image.new("1", (128, 64))
    draw = ImageDraw.Draw(image)

    # Check if the button is pressed (Feeding time!)
    if button.is_pressed:
        face = "(  ~O~ ) NOM"
    elif counter == 0:
        face = "( ^_^ )"
    elif counter == 1:
        face = "( O_o )"
    elif counter == 2:
        face = "( -_- )"
    elif counter == 3:
        face = "( >_< )"
    else:
        face = "( -.- )zZ"

    draw.text((35, 25), face, font=font, fill=255)
    oled.image(image)
    oled.show()

    # Only cycle to the next face if we aren't currently feeding
    if button.is_pressed == False:
        counter = counter + 1
        if counter > 4:
            counter = 0
    
    # Short delay to keep the button responsive
    time.sleep(0.2)