import asyncio
import os
import sys

# Check if the necessary environment variables are set
if not os.environ.get('DEVICE_ID') or \
   not os.environ.get('ACCOUNT_ID') or \
   not os.environ.get('SECRET'):
    print("Please set the DEVICE_ID, ACCOUNT_ID, and SECRET environment variables.\n")
    sys.exit()

# Install the required package
os.system("pip install -U klldFN")
os.system('clear')

import klldFN

# Get environment variables using os.environ.get
device_id = os.environ.get('DEVICE_ID')
account_id = os.environ.get('ACCOUNT_ID')
secret = os.environ.get('SECRET')

# Create the client instance
client = klldFN.klldFN(
    device_id=device_id,
    account_id=account_id,
    secret=secret
)

try:
    # Run the client
    client.run()
except Exception as e:
    print(e)
    print("Can't login because your device auths are probably wrong.")
