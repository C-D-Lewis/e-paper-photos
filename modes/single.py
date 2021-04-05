from PIL import Image
from modules import config, helpers

# Draw the single image
def draw(image):
  args = config.get('args')
  image_path = args['path']
  is_full_width = args['full_width'] == "true"

  loaded_image = Image.open(image_path)

  resized = helpers.fit_to_screen(image, loaded_image, is_full_width)

  image.paste(resized, (0, 0))
