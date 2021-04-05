# Fit image to screen height, optionally stretched horizontally
def fit_to_screen(image, loaded_image, is_full_width):
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
  return loaded_image.resize((target_w, target_h))
