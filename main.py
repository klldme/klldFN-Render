import asyncio
import os
import sys

if not os.environ.get('DEVICE_ID') and \
        not os.environ.get('ACCOUNT_ID') and \
        not os.environ.get('SECRET'):
    print("Please paste your device auths into the \"env\" file.\n")
    sys.exit()



os.system("pip install -U klldFN")
os.system('clear')

import klldFN

client = klldFN.klldFN(
  device_id=os.environ.get['DEVICE_ID'],  
  account_id=os.environ.get['ACCOUNT_ID'],
  secret=os.environ.get['SECRET']
)




try:
    client.run()
except Exception as e:
    print(e)
    print("Can't login because your device auths is probably wrong.")
