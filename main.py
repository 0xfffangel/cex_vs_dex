import asyncio
import multidex
import ccxt.async_support as ccxt
import argparse

def get_exchange(exchange):
    if exchange == 'binance':
        return ccxt.binance({'enableRateLimit': True})
    elif exchange == 'bitfinex':
        return ccxt.bitfinex({'enableRateLimit': True})
    elif exchange == 'kucoin':
        return ccxt.kucoin({'enableRateLimit': True})
    elif exchange == 'bybit':
        return ccxt.bybit({'enableRateLimit': True})
    elif exchange == 'ftx':
        return ccxt.ftx({'enableRateLimit': True})
    else:
        raise Exception("Exchange not supported")

def get_dex(dex):
    if dex == 'stellaswap':
        return multidex.Stellaswap()
    elif dex == 'uniswap':
        return multidex.Uniswap()
    elif dex == 'spookyswap':
        return multidex.Spookyswap()
    elif dex == 'pancakeswap':
        return multidex.Pancakeswap()
    elif dex == 'beamswap':
        return multidex.Beamswap()
    else:
        raise Exception("Dex not supported")

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--exchange", help = "Select exchange")
    parser.add_argument("-p", "--pair", help = "Select pair")
    parser.add_argument("-d", "--dex", help = "Select dex")
    parser.add_argument("-t", "--token", help = "Select token")
    return parser.parse_args()

async def main():

    args = get_arguments()
    exchange = get_exchange(args.exchange)
    ticker = await exchange.fetch_ticker(args.pair)
    print(args.exchange, " ask: ", ticker["ask"])
    print(args.exchange, " bid: ", ticker["bid"])
    print(args.exchange, " askVolume: ", ticker["askVolume"])
    print(args.exchange, " bidVolume: ", ticker["bidVolume"])
    print(args.exchange, " last: ", ticker["last"])
    await exchange.close()

    dex = get_dex(args.dex)
    print(args.dex, " reserve_ratio: ", dex.reserve_ratio(args.token))
    print(args.dex, " price: ", dex.price(args.token))
    print(args.dex, " liquidity: ", dex.liquidity(args.token))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())