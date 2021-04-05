import sys, time
from PIL import Image, ImageDraw

from modules import epaper, helpers, config
from modes import single

# Draw image from file
def handle_mode(image):
  mode = config.get('mode')

  # Show a single image and exit
  if 'single' in mode:
    single.draw(image)
    epaper.show(image)

    # Done
    time.sleep(2)
    epaper.sleep()
  else:
    raise Exception('Unknown mode')

# The main function
def main():
  config.load()
  image, image_draw = epaper.prepare()

  epaper.init()
  handle_mode(image)

if __name__ in '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Exiting')
    epaper.deinit()
    exit()
