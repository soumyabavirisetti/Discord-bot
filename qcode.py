import qrcode
from PIL import Image

def retqr(s):
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_H,
      box_size=10,
      border=4,
  )

  qr.add_data(s)
  qr.make(fit=True)

  img = qr.make_image(fill_color="black", back_color="white")
  img.save("qrcode.png")