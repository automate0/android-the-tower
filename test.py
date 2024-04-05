import os
from android_device import AndroidDevice
from time import sleep
from state import find_state
from PIL import Image, ImageDraw

device = AndroidDevice('emulator-5554')
app_package = 'com.TechTreeGames.TheTower'

cap = device.capture()
if cap is None:
    print('Capture failed')

#states = {
#    PlayAttackState(rects=[(10, 780, 140, 40), ], points={'damage': (300, 900), 'attack_speed': (600, 900)}),
#    PlayDefenseState(rects=[(10, 780, 140, 40), ]),
#    PlayUtilityState(rects=[(10, 780, 140, 40), ]),
#    GameOverState(rects=[(180, 1000, 100, 30), ], points={'retry': (230, 1020)})
#}

def draw_rectangles(image_path, rect):
    # Open the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Draw rectangle
    draw.rectangle(rect, outline="red")

    # Display the image
    img.show()

rect = (10, 140, 40, 780)
image_filename = 'screenshot.png'
script_dir = "C:\\Users\\Adam\\Pictures\\"
image_path = os.path.join(script_dir, image_filename)
draw_rectangles(image_path, rect)
