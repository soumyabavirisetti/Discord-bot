from PIL import Image
import requests
from io import BytesIO

#ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

#resize image according to a new width
def resize_image(image, new_width=100):
  width, height = image.size
  ratio = height / width
  new_height = int(new_width * ratio)
  resized_image = image.resize((new_width, new_height))
  return(resized_image)

#convert each pixel to grayscale
def grayify(image):
  grayscale_image = image.convert("L")
  return(grayscale_image)

#convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
  pixels = image.getdata()
  characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
  return(characters)

def asmain(url):
  new_width=100
  #attempt to open from user-input
  try:
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
  except:
    print("URL is not a valid to an image.")

  #convert image to ascii
  new_image_data = pixels_to_ascii(grayify(resize_image(image )))

  #format
  pixel_count = len(new_image_data)
  ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

  #print result
  return ascii_image

