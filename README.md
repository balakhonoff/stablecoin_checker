# stablecoin_checker
Telegram Bot that can find total balance of top-5 stablecoins in top-6 blockchains for EVM-compatible address

[![DEMO VIDEO](https://i.ibb.co/z5xSGT2/2022-03-31-13-12-46.png)](https://youtu.be/cheStgCaVLc)

Click [this link](https://youtu.be/cheStgCaVLc) to watch the demo video on YouTube

Check out the working bot in [telegram](https://t.me/stable_checker_bot)

---

**Installation**
Create a virtual environment
```
python3 -m venv web3env
```

Activate the virtual environment
```
. web3env/bin/activate
```

Clone the repository
```
git clone git@github.com:balakhonoff/stablecoin_checker.git
```

Go to the project folder
```
cd stablecoin_checker
```

Install the dependencies
```
pip install -r req_web3.txt
```

Create a bot token with botfather t.me/botfather according to instructions https://core.telegram.org/bots and assign the bot token to the variable `BOT_TOKEN`

Create an account in moralis.io to access speedy nodes for different blockchains and insert their urls to the variable
```
urls = {
    'eth': '<ETHEREUM_NODE>',
    'bsc': '<BSC_NODE>',
    'matic': '<MATIC_NODE>',
    'avax': '<AVAX_NODE>',
    'ftm': '<FANTOM_NODE>',
    'arb': '<ARBITRUM_NODE>'
}
```

Run the bot with command
```
python bot_check_balance.py
```

---

Usage

Send to the bot an address in usual format like 0xF977814e90dA44bFA03b6295A0616a897441aceC
which is one of the most rich USDT addresses from rating https://www.coincarp.com/currencies/tether/richlist/

and get the full stablecoin balance in all popular networks

