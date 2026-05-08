import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
from gpiozero import Button, LED

# --- Hardware Setup ---
# Initialize I2C and the OLED (assuming a standard 128x64 display)
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize GPIO Components
feed_button = Button(17, bounce_time=0.1)
play_button = Button(27, bounce_time=0.1)
sleep_led = LED(22)

# --- Pet Variables ---
hunger = 0      # 0 is full, 10 is starving
boredom = 0     # 0 is entertained, 10 is bored to tears
is_asleep = False

# Timers
last_update_time = time.time()
UPDATE_INTERVAL = 5 # How many seconds before stats increase (make it longer for real life!)

# Load a default font for drawing text
font = ImageFont.load_default()

def draw_pet(face, status_text):
    """Clears the screen, draws the face and text, and updates the OLED."""
    # Create a blank image for drawing
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    
    # Draw the face in the middle and status at the bottom
    draw.text((35, 20), face, font=font, fill=255)
    draw.text((10, 50), status_text, font=font, fill=255)
    
    # Send image to OLED
    oled.image(image)
    oled.show()

def feed_pet():
    global hunger
    if not is_asleep:
        hunger = max(0, hunger - 3) # Decrease hunger, don't go below 0
        draw_pet("( ^o^ )", "Yum! Thanks!")
        time.sleep(1)

def play_with_pet():
    global boredom
    if not is_asleep:
        boredom = max(0, boredom - 3)
        draw_pet("\\( ^_^ )/", "Wheee!")
        time.sleep(1)

# Attach button functions
feed_button.when_pressed = feed_pet
play_button.when_pressed = play_with_pet

# --- Main Game Loop ---
print("Desk pet is alive! Press Ctrl+C to exit.")

try:
    while True:
        current_time = time.time()
        
        # Check if it's time for the pet's stats to get worse
        if current_time - last_update_time > UPDATE_INTERVAL:
            hunger += 1
            boredom += 1
            last_update_time = current_time
            
        # Determine Pet Status and Face
        if hunger >= 15 or boredom >= 15:
            # Pet goes to sleep to escape neglect
            is_asleep = True
            sleep_led.on()
            draw_pet("( -.- )zZ", "Sleeping...")
            # Sleep acts as a reset after a while
            time.sleep(5) 
            hunger = 0
            boredom = 0
            is_asleep = False
            sleep_led.off()
            
        elif hunger >= 7:
            draw_pet("( O_o )", f"Hungry! (H:{hunger})")
        elif boredom >= 7:
            draw_pet("( -_- )", f"Bored... (B:{boredom})")
        else:
            draw_pet("( ^_^ )", f"Happy! (H:{hunger} B:{boredom})")
            
        time.sleep(0.1) # Small delay to prevent maxing out the CPU

except KeyboardInterrupt:
    # Clean up the screen on exit
    oled.fill(0)
    oled.show()
    print("\nDesk pet went bye-bye.")