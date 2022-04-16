# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import pyzbar.pyzbar as pyz
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import gzip
import base64


priv_pem = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDFLr+Lm7dle9QPSMrevd7c+8rjalImu6htMCNz/rV9Npzh8ynL
0ued9hNgm9J7rnkB+gZBk8oasBjThykaqnSC7XIj0nnHxHQld9p/SvOnxu0u9Wg3
o/evxTcy2hsIHKPsomrbuxBOCw/68HU55AFulUpskKndhLKa4biQX/W1FQIDAQAB
AoGACQh+4+wVTG6OJMkb6h+z/FcDUMRye63F0IK6YmT9IX2wADXok0WChjJbaZCZ
5ZVKRonoDCGzdOIzsPUUhVE2bHhq9O7OnIUTW+geS2zEG0aFVA0JQ4DMEzHl9fzh
yNZU6zDUmyvyuISmQJRCIG3yUdjnEstf65T4pxSDr9//0AECQQDOg7wl6T7C4d/k
paBvYN9g1UujvSOlQivP7IMtBy/bGvyMy8zvc0cTzcPBGYOksRi9ihHhOyKyAjpO
8efjddQBAkEA9G6PUKD2vjiD+mtWmIlfGO6ZMN7Ylkr9PRLCwsh+Hmz7iBhrxkAw
Qqd+SFaQzxEkQVjdrI7LO2B6SARF4zdRFQJAQqcB8rp1JzD/sixCu6/oaLhu0Uoa
VxwkR9dt/vpy16S+HjMo0Z/DMQEYTRqPAnimI4aMfsU3TXyqlRA+Z4uAAQJBAJTW
JYoxGU3m1+ZKKeaj7zYdQ0aQy01oyB7CJ7m3n6QjNF5AkI+dUkWj+69MlsyfYXYx
CHokUPgM3SixAWVDr6kCQGP2N1uzULQDfA7kIQmmJvZfXyy2xr/3RxQ25j++4i6b
aFh+t3hRXY3l1SVOKtumfQYSqFquIfeAiSbszW9J0P4=
-----END RSA PRIVATE KEY-----"""

priv_key = RSA.import_key(priv_pem)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    vid = cv2.VideoCapture(0)
    vid.set(3, 640)
    vid.set(4, 480)
    qrDecoder = cv2.QRCodeDetector()


    while(True):
        success, frame = vid.read()

        for barcode in pyz.decode(frame):

            d = barcode.data.decode("ascii")
            print(d)

            bbb = base64.b64decode(d)

            cipher = PKCS1_OAEP.new(priv_key)
            message = cipher.decrypt(bbb)

            d_dec = gzip.decompress(message)
            print(d_dec)

        cv2.imshow("Result", frame)
        cv2.waitKey(1)





a = 4
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
