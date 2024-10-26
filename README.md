# Trenches-Bot
Trenches Project with Reymus

V1.0
- Scan as many wallets as you want, just need to input them into the code under wallet_address
- Up to 10 most recent transactions
- Once the bot does one round of checking and repeats, it will only take the MOST RECENT transaction and cross check it against the first transaction of the previous batch. If its the same transaction, no new transaction is made and the bot skips the wallet proceeding to the new one. This ensures minimal use of API points
- Able to identify Raydium V4
- Pumpfun identification still unstable
- Integrated with Telegram bot
- Currently 240 API points used per minute
