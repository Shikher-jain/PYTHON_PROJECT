
from barcode import EAN13

# The number to be converted into a barcode
number = '5901234123457'

# Generating the barcode
my_code = EAN13(number)

# Saving the barcode as an image
my_code.save('Shikher-jain/PROJECTs/ean13_barcode_image')