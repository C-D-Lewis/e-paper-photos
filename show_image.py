import platform, sys, os, time
from PIL import Image, ImageDraw

RUNNING_ON_PI = 'arm' in platform.machine()
print({ 'RUNNING_ON_PI': RUNNING_ON_PI })

IMAGE_PATH = sys.argv[1]
FULL_WIDTH = len(sys.argv) == 3 and sys.argv[2] == '-f'

# Only runs on Pi
if RUNNING_ON_PI:
  from lib.waveshare_epd import epd7in5_V2
  epd = epd7in5_V2.EPD()
  disp_width = epd.width
  disp_height = epd.height
else:
  print('[TEST] EPD import')
  disp_width = 800
  disp_height = 480

################################## Testability #################################

# Initialise the display
def init_display():
  if RUNNING_ON_PI:
    epd.init()
  else:
    print('[TEST] epd.init()')

# Handle updating the display
def update_display(image):
  if RUNNING_ON_PI:
    epd.display(epd.getbuffer(image))
  else:
    image.save('render.png')
    print('[TEST] epd.display()')

# Handle sleeping the display
def sleep_display():
  if RUNNING_ON_PI:
    epd.sleep()
  else:
    print('[TEST] epd.sleep()')

# Handle deinitialising the display
def deinit_display():
  if RUNNING_ON_PI:
    epd7in5_V2.epdconfig.module_exit()
  else:
    print('[TEST] module_exit()')

################################## Main loop ###################################

# Draw things
def draw():
  # Prepare
  image = Image.new('1', (disp_width, disp_height), 255)  # Mode = 1bit
  canvas = ImageDraw.Draw(image)
  canvas.rectangle((0, 0, disp_width, disp_height), fill = 255)

  # Open image
  loaded_image = Image.open(IMAGE_PATH)

  # Resize to fill height and width
  image_w, image_h = loaded_image.size
  target_w = image_w
  target_h = image_h
  image_ratio = float(image_w / image_h)
  if target_h > disp_height:
    target_h = disp_height
  target_w = round(image_ratio * target_h)

  # If full width requested
  if FULL_WIDTH == True:
    target_w = disp_width
    target_h = round(target_w / image_ratio)

  # Apply resize
  resized = loaded_image.resize((target_w, target_h))

  # Draw image
  image.paste(resized, (0, 0))

  # Update display
  update_display(image)
  time.sleep(2)

# Update all the things
def update():
  pass

# The main function
def main():
  update()
  init_display()
  draw()
  sleep_display()

if __name__ in '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Exiting')
    deinit_display()
    exit()
