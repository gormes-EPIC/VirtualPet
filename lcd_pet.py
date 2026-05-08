import time
from RPLCD.i2c import CharLCD
from gpiozero import Button, LED

# --- Hardware Setup ---
# Initialize the LCD. 
# Note: I2C addresses are typically 0x27 or 0x3F. Change if necessary.
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)

# Initialize GPIO Components
feed_button = Button(17, bounce_time=0.1)
play_button = Button(27, bounce_time=0.1)
sleep_led = LED(22)

# --- Pet Variables ---
hunger = 0      
boredom = 0     
is_asleep = False

# Timers
last_update_time = time.time()
UPDATE_INTERVAL = 5 

def draw_pet(face, status_text):
    """Clears the screen and prints the face and text."""
    lcd.clear()
    
    # Center the face on the top line (Line 0)
    # A 16x2 LCD has 16 characters per line. We calculate padding to center it.
    padding = (16 - len(face)) // 2
    lcd.cursor_pos = (0, padding)
    lcd.write_string(face)
    
    # Write the status on the bottom line (Line 1)
    lcd.cursor_pos = (1, 0)
    # The [:16] ensures the text never overflows the 16-character limit
    lcd.write_string(status_text[:16]) 

def feed_pet():
    global hunger
    if not is_asleep:
        hunger = max(0, hunger - 3) 
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
            is_asleep = True
            sleep_led.on()
            draw_pet("( -.- )zZ", "Sleeping...")
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
            # Keep text short to fit on 16 characters!
            draw_pet("( ^_^ )", f"Happy! H:{hunger} B:{boredom}")
            
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up the screen on exit
    lcd.clear()
    lcd.close(clear=True)
    print("\nDesk pet went bye-bye.")