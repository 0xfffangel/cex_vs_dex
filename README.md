SpreadBot
===

Python price bot for a single pair on CEX (=exchanges) and DEX (=swaps).

Based on [ccxt](https://github.com/ccxt/ccxt) and [multidex-python](https://github.com/0xfffangel/multidex-python).

### Install
```bash
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Example
```bash
python main.py -e binance -p GLMRBUSD -d stellaswap -t 0xa649325aa7c5093d12d6f98eb4378deae68ce23f
binance ask:  5.8917
binance bid:  5.8744
binance last:  5.8842
stellaswap reserve_ratio:  5.888175633083993
stellaswap price:  5.870494361488615
```