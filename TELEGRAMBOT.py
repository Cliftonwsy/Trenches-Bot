import telebot
import time
import base58
import re
from dotenv import load_dotenv
import os
from solana.rpc.api import Client
from solders.pubkey import Pubkey
from solders.signature import Signature
from solana.exceptions import SolanaRpcException
import requests
import logging
from jsonrpcclient import request, parse, Ok

load_dotenv()
SOLANA_KEY = os.getenv('SOLANA_KEY')
TELEBOT_API_KEY = os.getenv('TELEBOT_API_KEY')
bot = telebot.TeleBot(TELEBOT_API_KEY)

wallet_address = [
    '6xuMV6W6QVxrVmsZxEdLfV6kfhuBsg3ah1X8rydLfQvy',
    'Hd9HKLie1nKXx4zLQXg9WVYyK95kBFEC7bj1aGwRtBqF',
]
repeated_lists = {wallet: ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'] for wallet in wallet_address}
first_tx_list = ['1', '1', '1']

@bot.message_handler(commands=['startbot'])
def start(message):
    print("started")
    bot.send_message(message.chat.id,"Bot started 🤖")
    while True:
        for i in range(len(wallet_address)):
            time.sleep(10)
            try:
                print(f"checking wallet {int(i) + 1}")
                decoded_wallet = base58.b58decode(wallet_address[i])
                address = Pubkey(decoded_wallet)
                identified_list = [[] for _ in wallet_address]
                solana_client = Client(SOLANA_KEY)
                #check for new transactions
                transaction_history = solana_client.get_signatures_for_address(address, limit=1)
                transaction_history = str(transaction_history)
                signatures = re.findall(r'signature: "([A-Za-z0-9]+)"', transaction_history)
                sig = Signature.from_string(signatures[0])
                if str(sig).strip() == first_tx_list[i].strip():
                    print(f"wallet {int(i) + 1} no new transactions.")
                    continue
                first_tx_list[i] = str(sig)
                transaction_history = solana_client.get_signatures_for_address(address, limit=10)
                transaction_history = str(transaction_history)
                signatures = re.findall(r'signature: "([A-Za-z0-9]+)"', transaction_history)
                n = 0
                for j in range(len(signatures)):
                    sig = Signature.from_string(signatures[j])
                    extracted_info = solana_client.get_transaction(sig, "jsonParsed", max_supported_transaction_version=0)
                    #check for raydium
                    if "5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1" in str(extracted_info):
                        identified_list[i].append(signatures[j])
                        n+=1
                        for x in range(n):
                            solana_client = Client(SOLANA_KEY)
                            sig = Signature.from_string(identified_list[i][x])
                            info = solana_client.get_transaction(sig, "jsonParsed", max_supported_transaction_version=0)
                            if "account_index: 2" in str(info) and identified_list[i][x] not in repeated_lists[wallet_address[i]]:
                                pattern = r'account_index: 2, mint: "([^"]+)"'
                                match = re.search(pattern, str(info))
                                url = f"https://api.jup.ag/price/v2?ids={match.group(1)}"
                                response = requests.get(url, params={'token': 'USDC'})
                                if response.status_code == 200:
                                    data = response.json()
                                    if 'data' in data and match.group(1) in data['data']:
                                        price = data['data'][match.group(1)]['price']
                                        response = requests.post(SOLANA_KEY, json=request("getTokenSupply", params=([match.group(1)])))
                                        parsed = parse(response.json())
                                        if isinstance(parsed, Ok):
                                            token_supply = int(parsed.result['value']['amount'])
                                            decimals = int(parsed.result['value']['decimals'])
                                            human_readable_supply = token_supply / (10 ** decimals)
                                            human_readable_supply = float(human_readable_supply)
                                            price = float(price)
                                            print(human_readable_supply)
                                            print(price)
                                            market_cap = human_readable_supply * price
                                        else:
                                            logging.error(parsed.message)
                                    else:
                                        print(f"Error: Token {match.group(1)} not found in the response.")
                                else:
                                    print("Error:", response.status_code)
                                if match.group(1) == "So11111111111111111111111111111111111111112":
                                    continue
                                else:
                                    escaped_market_cap = str(market_cap).replace('.', '\\.')
                                    bot.send_message(message.chat.id, 
                                                     f"💰 *MEMECOIN BUY ALERT* 💰\n\n"
                                                     f"💳 *WALLET NAME:* 💳\nWALLET {int(i) + 1}\n\n"
                                                     f"🔑 *TRANSACTION:* 🔑\n{identified_list[i][x]}\n"
                                                     f"🔒 RAYDIUM V4 🔒\n\n"
                                                     f"🚀 *TOKEN ID:* 🚀\n{match.group(1)}\n\n"
                                                     f"💲 *MARKET CAP:* 💲\nUSD {escaped_market_cap}",
                                                     parse_mode='MarkdownV2')
                                    repeated_lists[wallet_address[i]][x] = identified_list[i][x]
                            elif "account_index: 2" not in str(info):
                                continue
                    #check for pumpfun
                    elif "4wTV1YmiEkRvAtNtsSGPtUrqRYQMe5SKy2uB4Jjaxnjf" in str(extracted_info):
                        identified_list[i].append(signatures[j])
                        n+=1
                        for x in range(n):
                            solana_client = Client(SOLANA_KEY)
                            sig = Signature.from_string(identified_list[i][x])
                            info = solana_client.get_transaction(sig, "jsonParsed", max_supported_transaction_version=0)
                            if "account_index: 6" in str(info) and identified_list[i][x] not in repeated_lists[wallet_address[i]]:
                                pattern = r'account_index: 6, mint: "([^"]+)"'
                                match = re.search(pattern, str(info))
                                url = f"https://api.jup.ag/price/v2?ids={match.group(1)}"
                                response = requests.get(url, params={'token': 'USDC'})
                                if response.status_code == 200:
                                    data = response.json()
                                    if 'data' in data and match.group(1) in data['data']:
                                        price = data['data'][match.group(1)]['price']
                                        response = requests.post(SOLANA_KEY, json=request("getTokenSupply", params=([match.group(1)])))
                                        parsed = parse(response.json())
                                        if isinstance(parsed, Ok):
                                            token_supply = int(parsed.result['value']['amount'])
                                            decimals = int(parsed.result['value']['decimals'])
                                            human_readable_supply = token_supply / (10 ** decimals)
                                            human_readable_supply = float(human_readable_supply)
                                            price = float(price)
                                            market_cap = human_readable_supply * price
                                        else:
                                            logging.error(parsed.message)
                                    else:
                                        print(f"Error: Token {match.group(1)} not found in the response.")
                                else:
                                    print("Error:", response.status_code)
                                if match.group(1) == "So11111111111111111111111111111111111111112":
                                    continue
                                else:
                                    escaped_market_cap = str(market_cap).replace('.', '\\.')
                                    bot.send_message(message.chat.id, 
                                                     f"💰 *MEMECOIN BUY ALERT* 💰\n\n"
                                                     f"💳 *WALLET NAME:* 💳\nWALLET {int(i) + 1}\n\n"
                                                     f"🔑 *TRANSACTION:* 🔑\n{identified_list[i][x]}\n"
                                                     f"✊ PUMPFUN ✊\n\n"
                                                     f"🚀 *TOKEN ID:* 🚀\n{match.group(1)}\n\n"
                                                     f"💲 *MARKET CAP:* 💲\nUSD {escaped_market_cap}",
                                                     parse_mode='MarkdownV2')
                                    repeated_lists[wallet_address[i]][x] = identified_list[i][x]
                            elif "account_index: 6" not in str(info):
                                continue
                    #if got none
                    elif "5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1" not in str(extracted_info) or "4wTV1YmiEkRvAtNtsSGPtUrqRYQMe5SKy2uB4Jjaxnjf" not in str(extracted_info):
                        continue

            except (SolanaRpcException, Exception) as e:  # Added error handling
                print(f"An error occurred: {e}")  # Print the error message
                print("Retrying immediately...")  # Message before retrying
                continue

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(message.chat.id,"✅")

bot.polling(timeout=120, long_polling_timeout=120)