from jsonrpcclient import request, parse, Ok
import logging
import requests
response = requests.post("https://long-patient-thunder.solana-mainnet.quiknode.pro/489b5d8fac89460c8e91f249eac9ee2b6a83e1e2/", json=request("getTokenSupply", params=(["7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU"])))
parsed = parse(response.json())
if isinstance(parsed, Ok):
    token_supply = int(parsed.result['value']['amount'])
    decimals = int(parsed.result['value']['decimals'])
    human_readable_supply = token_supply / (10 ** decimals)
    print(f"Human Readable Token Supply: {human_readable_supply}")
else:
    logging.error(parsed.message)