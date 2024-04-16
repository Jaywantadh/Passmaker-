# -*- coding: utf-8 -*-
"""QR_code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jtjxk8vSS33YpGJknsFKizrJ14e_me-x
"""

import pandas as pd
import qrcode
import csv
from PIL import Image
import passmaker as p
import emailsender as em

def generate_qr_codes():
        df= pd.read_csv('')
        Logo_link = 'logo.png'
        logo = Image.open(Logo_link)
        basewidth = 100
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize))
        for index, row in df.iterows():
            data = f"{row['']} \n{row['']} "  # Change this to the data you want to encode in the QR code
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            img.paste(logo, pos)
            filename = f"{row['']]}.png"
            img.save(filename)
            print(f"{filename}")


p.create_passes()
if __name__ == "__main__":
    generate_qr_codes()