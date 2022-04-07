import pyqrcode
import png
from pyqrcode import QRCode

link = 'https://coinmarketcap.com/historical/20210103/'
url = pyqrcode.create(link)
url.png('bitcoin_history.png', scale = 10)