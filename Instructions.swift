"""

Get recent transaction based on wallet, limit = how many recent
This is only for TRANSACTIONS not transfer

import base58
from solana.rpc.api import Client
from solders.pubkey import Pubkey

wallet_address = '6qBMtRQpQotxEgDRsUZ9DDnZoFxBf9MxxLPs4CG6yKrv'
decoded_bytes = base58.b58decode(wallet_address)
solana_client = Client(SOLANA_KEY)

print(len(decoded_bytes)) #32 bytes

address = Pubkey(decoded_bytes)
print(solana_client.get_signatures_for_address(address, limit=10))

"""
"""

Get account info only checks the balance on the account now

from solana.rpc.api import Client
from solders.pubkey import Pubkey
import base58

wallet_address = '6qBMtRQpQotxEgDRsUZ9DDnZoFxBf9MxxLPs4CG6yKrv'
decoded_bytes = base58.b58decode(wallet_address)
solana_client = Client(SOLANA_KEY)
print(solana_client.get_account_info(Pubkey(decoded_bytes)))

"""
"""
Check Transaction

from solana.rpc.api import Client
from solders.signature import Signature
solana_client = Client(SOLANA_KEY)
sig = Signature.from_string("28WMBsfy4QQGW4ZSPUkN2DcbBdxXdfXKFKvTvR8m2PodndC3Btzo8WTgQM77HvP3eaGxGpX3LLEvqrTxVFC1SKdF")
print(solana_client.get_transaction(sig, "jsonParsed", max_supported_transaction_version=0))

"""

loop = asyncio.new_event_loop()  # Create a new event loop
    asyncio.set_event_loop(loop)  # Set it as the current loop
    result = loop.run_until_complete(QuicknodeSolana.CHECK_TRANSACTION_HISTORY(wallet))

for x in range(n):
                    solana_client = Client(SOLANA_KEY)
                    sig = Signature.from_string(identified_list[i][x])
                    info = solana_client.get_transaction(sig, "jsonParsed", max_supported_transaction_version=0)
                    if "account_index: 2" in str(info) and identified_list[i][x] not in repeated_lists[wallet_address[i]]:
                        pattern = r'account_index: 2, mint: "([^"]+)"'
                        match = re.search(pattern, str(info))
                        bot.send_message(message.chat.id, f"💰MEMECOIN BUY ALERT💰\n 💳FROM WALLET {int(i) + 1}💳\n 🚀TOKEN ID: {match.group(1)}🚀")
                        repeated_lists[wallet_address[i]][x] = identified_list[i][x]
                    elif "account_index: 6" in str(info) and identified_list[i][x] not in repeated_lists[wallet_address[i]]:
                        pattern = r'account_index: 6, mint: "([^"]+)"'
                        match = re.search(pattern, str(info))
                        bot.send_message(message.chat.id, f"💰MEMECOIN BUY ALERT💰\n 💳FROM WALLET {int(i) + 1}💳\n 🚀TOKEN ID: {match.group(1)}🚀")
                        repeated_lists[wallet_address[i]][x] = identified_list[i][x]
                    elif "account_index: 2" not in str(info):
                        continue
                print("done")
"""
get token supply

from jsonrpcclient import request, parse, Ok
import logging
import requests
response = requests.post("", json=request("getTokenSupply", params=(["7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU"])))
parsed = parse(response.json())
if isinstance(parsed, Ok):
    print(parsed.result)
else:
    logging.error(parsed.message)
"""

"""
get price

import requests

# Your Jupiter API URL (replace with your actual URL)
url =

# Make a GET request to the price endpoint
response = requests.get(url, params={
    'token': 'USDC'  # Example token
})

# Parse and display the response
if response.status_code == 200:
    data = response.json()
    print("Token Price:", data)
else:
    print("Error:", response.status_code)
"""