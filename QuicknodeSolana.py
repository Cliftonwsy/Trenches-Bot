import base58
from solana.rpc.api import Client
from solders.pubkey import Pubkey
from solders.signature import Signature
import re
from dotenv import load_dotenv
import os

SOLANA_KEY = os.getenv('SOLANA_KEY')
wallet_address = 'Gxvi21TQFxfSYQnonZadATrpDvCx9tNjpxpzV2EN5Ays'
decoded_bytes = base58.b58decode(wallet_address)
solana_client = Client(SOLANA_KEY)

print(len(decoded_bytes)) #32 bytes

address = Pubkey(decoded_bytes)
transaction_history = solana_client.get_signatures_for_address(address, limit=1)
transaction_history = str(transaction_history)
signatures = re.findall(r'signature: "([A-Za-z0-9]+)"', transaction_history)
sig = Signature.from_string(signatures[0])
print(signatures)
print(sig)