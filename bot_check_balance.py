from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
from web3 import Web3

BOT_TOKEN="<INSERT_YOUR_BOT_TOKEN>"  # you can create a bot token via t.me/botfather

# the blockchains
networks = ['eth', 'bsc', 'matic', 'avax', 'ftm', 'arb']

#the names of blockchains
netnames = {
    'eth': 'Ethereum',
    'bsc': 'Binance Smart Chain',
    'matic': 'Polygon',
    'avax': 'Avalanche',
    'ftm': 'Fantom',
    'arb': 'Arbitrum'
}

#Insert urls for your nodes (you can user free moralis.io speedy nodes)
urls = {
    'eth': '<ETHEREUM_NODE>',
    'bsc': '<BSC_NODE>',
    'matic': '<MATIC_NODE>',
    'avax': '<AVAX_NODE>',
    'ftm': '<FANTOM_NODE>',
    'arb': '<ARBITRUM_NODE>'
}

#list of popular stablecoins
currs = [
    'USDT', 'BUSD', 'USDC', 'DAI', 'UST'
]
# addresses of smart contracts of this stablecoins in different blockchains
contracts = {
    'eth': {'USDT': '0xdac17f958d2ee523a2206206994597c13d831ec7',
            'BUSD': '0x4Fabb145d64652a948d72533023f6E7A623C7C53',
            'USDC': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
            'DAI': '0x6b175474e89094c44da98b954eedeac495271d0f',
            'UST': '0xa47c8bf37f92aBed4A126BDA807A7b7498661acD'},
    'bsc': {'USDT': '0x55d398326f99059ff775485246999027b3197955',
            'BUSD': '0xe9e7cea3dedca5984780bafc599bd69add087d56',
            'USDC': '0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d',
            'DAI': '0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3',
            'UST': '0x23396cf899ca06c4472205fc903bdb4de249d6fc'},
    'matic': {'USDT': '0xc2132d05d31c914a87c6611c10748aeb04b58e8f',
            'BUSD': '0xa8d394fe7380b8ce6145d5f85e6ac22d4e91acde',
            'USDC': '0x2791bca1f2de4661ed88a30c99a7a9449aa84174',
            'DAI': '0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063',
            'UST': '0xE6469Ba6D2fD6130788E0eA9C0a0515900563b59'},
    'avax': {'USDT': '0xc7198437980c041c805a1edcba50c1ce5db95118',
            'BUSD': '0x19860CCB0A68fd4213aB9D8266F7bBf05A8dDe98',
            'USDC': '0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E',
            'DAI': '0xd586E7F844cEa2F87f50152665BCbc2C279D8d70',
            'UST': '0xb599c3590F42f8F995ECfa0f85D2980B76862fc1'},
    'ftm': {'USDT': '0x049d68029688eabf473097a2fc38ef61633a3c7a',
            # 'BUSD': '',
            'USDC': '0x04068DA6C83AFCFA0e13ba15A6696662335D5B75',
            'DAI': '0x8D11eC38a3EB5E956B052f67Da8Bdc9bef8Abf3E',
            # 'UST': ''
            },
    'arb': {'USDT': '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
            # 'BUSD': '',
            'USDC': '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
            'DAI': '0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1',
            # 'UST': ''
            }
}

#decimals for every blockchain and every smart contract
decimals = {
    'eth': {'USDT': 6,
            'BUSD': 18,
            'USDC': 6,
            'DAI': 18,
            'UST': 18},
    'bsc': {'USDT': 18,
            'BUSD': 18,
            'USDC': 18,
            'DAI': 18,
            'UST': 18},
    'matic': {'USDT': 6,
            'BUSD': 18,
            'USDC': 6,
            'DAI': 18,
            'UST': 6},
    'avax': {'USDT': 6,
            'BUSD': 18,
            'USDC': 6,
            'DAI': 18,
            'UST': 6},
    'ftm': {'USDT': 6,
            # 'BUSD': ,
            'USDC': 6,
            'DAI': 18,
            # 'UST':
            },
    'arb': {'USDT': 6,
            # 'BUSD': ,
            'USDC': 6,
            'DAI': 18,
            # 'UST':
            },
}

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Send me an address of metamask account (Ethereum, Binance Smart Chain, Polygon, Avalanche, Fantom, Arbitrum), and I will check if there are stablecoins (USDT, BUSD, USDC, DAI, UST) at this address in all networks and in what quantity.')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def check_balance(address):
    try:
        result_str = ""
        total_sum = 0
        for net in networks:
            moralis_url = urls[net]
            provider = Web3.HTTPProvider(moralis_url)
            web3 = Web3(provider)
            # print(web3.isConnected())
            if web3.isConnected():
                print(f'Connected to {netnames[net]}')
                for cur in currs:
                    # print(f'Finding {cur}...')
                    if cur in contracts[net].keys():
                        abi = json.loads(
                            '[{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
                        # abi = json.loads(abis[net][cur])
                        contract = web3.eth.contract(address=Web3.toChecksumAddress(contracts[net][cur]), abi=abi)
                        balance = contract.functions.balanceOf(address).call() / (10 ** decimals[net][cur])
                        if balance > 0:
                            print(f'Found {balance}{cur} at {netnames[net]}')
                            result_str += f'Found {balance:.2f} {cur} at {netnames[net]}\n'
                            total_sum += balance
            else:
                print(f'Failed to connect {netnames[net]}, skipped.')

        result_str += f"\nTotal stablecoin sum is {total_sum:.2f} USD"
        return result_str
    except:
        return None

def echo(update, context):
    """Echo the user message."""
    try:
        txt = update.message.text.strip()
        if len(txt) == 42:
            if txt[:2] == '0x':
                if txt[2:].isalnum():
                    update.message.reply_text('Finding...')
                    result_str = check_balance(txt)
                    if result_str != None:
                        update.message.reply_text(result_str)
                        return
                    else:
                        update.message.reply_text("Sorry, the calculation failed. Please contact the developer @chan_owner")
                        return
        update.message.reply_text('Bad format of address.\nThe correct format of address example: 0xbAbF38eda83a14757ABEe659780a887119F8dB0b')
    except:
        print('error')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # # log all errors
    # dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
