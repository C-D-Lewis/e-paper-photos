import sys, time
from PIL import Image, ImageDraw

from modules import fetch, epaper

# Draw image from file
def draw_top_today_image(image, ):
  # Open image
  loaded_image = Image.open(path)

  # Resize to fill height and width
  image_w, image_h = loaded_image.size
  target_w = image_w
  target_h = image_h
  image_ratio = float(image_w / image_h)
  if target_h > image.height:
    target_h = image.height
  target_w = round(image_ratio * target_h)

  # If full width requested
  if is_full_width == True:
    target_w = image.width
    target_h = round(target_w / image_ratio)

  # Apply resize
  resized = loaded_image.resize((target_w, target_h))

  # Draw image
  image.paste(resized, (0, 0))

# Draw things
def draw():
  path = sys.argv[1]
  is_full_width = len(sys.argv) >= 3 and '-f' in sys.argv

  image, image_draw = epaper.prepare()

  draw_top_today_image(image, path, is_full_width)

  epaper.show(image)
  time.sleep(2)

# The main function
def main():
  epaper.init()
  draw()
  epaper.sleep()

if __name__ in '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Exiting')
    epaper.deinit()
    exit()
