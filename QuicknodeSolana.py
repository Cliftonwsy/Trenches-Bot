from dotenv import load_dotenv
import os

from solana.rpc.api import Client
from solders.signature import Signature

load_dotenv()
SOLANA_KEY = os.getenv('SOLANA_KEY')
TELEBOT_API_KEY = os.getenv('TELEBOT_API_KEY')

solana_client = Client(SOLANA_KEY)
sig = Signature.from_string("3QrzMgFFJ6VdNkCAF7A1dB23T9mGv1KUhzhqvv3DS3oLLhWFyivPrCLyj1XL28To3bMFEwdPZLPuZxfVmrz3FSFp")
print(solana_client.get_transaction(sig, "jsonParsed", max_supported_transaction_version=0))

