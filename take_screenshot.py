import os
from android_device import AndroidDevice
from PIL import Image, ImageDraw

# Find android device
device = AndroidDevice('emulator-5554')

# Capture image
cap = device.capture()
if cap is None:
    print('Capture failed')

# Save image
image_filename = 'screenshot'
image_suffix = ".png"
script_dir = r"D:\Git_Projects\Gaminig\TheTower\bjyxm_bot\screenshots"
image_path = os.path.join(script_dir, image_filename + image_suffix)
print(image_path)

cap.save(image_path)

def draw_rectangles(image_path, rect):
    # Open the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Draw rectangle
    draw.rectangle(rect, outline="red")

    # Display the image
    img.show()

#rect = (10, 780, 40, 40)
#draw_rectangles(image_path, rect)

#capture.crop((10, 780, 150, 820)).show()