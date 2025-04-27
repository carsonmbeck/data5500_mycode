
#!/usr/bin/env python3
import os
import json
from datetime import datetime
import requests
import networkx as nx
from alpaca_trade_api.rest import REST
from dotenv import load_dotenv


load_dotenv()
API_KEY       = os.getenv("ALPACA_API_KEY")
SECRET_KEY    = os.getenv("ALPACA_SECRET_KEY")
BASE_URL      = os.getenv("ALPACA_PAPER_API_URL", "https://paper-api.alpaca.markets")
DATA_DIR      = "/home/ubuntu/data"
RESULTS_FILE  = "/home/ubuntu/results.json"
THRESHOLD     = 1.0005   # only trade if factor > 1.0005

os.makedirs(DATA_DIR, exist_ok=True)

def ts():
    return datetime.utcnow().strftime("%Y.%m.%d:%H.%M")

def save_raw(data):
    fn = f"{DATA_DIR}/currency_pair_{ts()}.txt"
    with open(fn, "w") as f:
        f.write("currency_from,currency_to,exchange_rate\n")
        for src, rates in data.items():
            for dst, rate in rates.items():
                f.write(f"{src},{dst},{rate}\n")
    return fn

def find_triangles(g):
    best = {"factor": 1.0, "cycle": None}
    worst= {"factor": float("inf"), "cycle": None}
    for a in g.nodes():
        for b in g.successors(a):
            for c in g.successors(b):
                if g.has_edge(c, a):
                    f = g[a][b]['weight'] * g[b][c]['weight'] * g[c][a]['weight']
                    if f > best["factor"]:
                        best = {"factor": f, "cycle": (a, b, c)}
                    if f < worst["factor"]:
                        worst= {"factor": f, "cycle": (a, b, c)}
    return best, worst

def place_order(api, symbol, side, qty):
    try:
        o = api.submit_order(symbol=symbol, side=side, type="market", qty=qty, time_in_force="gtc")
        print(f"→ {side} {qty} {symbol} (id={o.id})")
    except Exception as e:
        print(f"Order failed: {e}")

# MAIN logc
def main():
    coins = [
      "bitcoin","ethereum","litecoin","ripple","cardano","bitcoin-cash","eos",
      "dogecoin","polkadot","chainlink","stellar","solana","theta-token"
    ]
    vs = ",".join(["btc","eth","ltc","xrp","ada","bch","eos","doge","dot","link","xlm","sol","theta"])
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies={vs}"
    data = requests.get(url).json()

    # 2 Save raw pairs
    raw_file = save_raw(data)
    print(f"Saved raw pairs → {raw_file}")

    id2tick = {
      "bitcoin":"btc","ethereum":"eth","litecoin":"ltc","ripple":"xrp",
      "cardano":"ada","bitcoin-cash":"bch","eos":"eos",
      "dogecoin":"doge","polkadot":"dot","chainlink":"link",
      "stellar":"xlm","solana":"sol","theta-token":"theta"
    }
    g = nx.DiGraph()
    for cid, rates in data.items():
        src = id2tick[cid]
        for dst, rate in rates.items():
            if dst != src and dst in id2tick.values():
                g.add_edge(src, dst, weight=rate)

    # 4) Find best/worst triangular arbitrage
    best, worst = find_triangles(g)
    print("Best triangle:", best)
    print("Worst triangle:", worst)

    # 5) Paper-trade if above threshold
    api = REST(API_KEY, SECRET_KEY, BASE_URL)
    if best["factor"] > THRESHOLD:
        a,b,c = best["cycle"]
        print(f"Executing triangle trade: {a}→{b}→{c}→{a}, factor={best['factor']:.4f}")
        place_order(api, f"{a.upper()}USD",   "buy", 10)  # $10 into a

    # 6) Write results.json
    summary = {
      "timestamp": datetime.utcnow().isoformat(),
      "best_triangle": best,
      "worst_triangle": worst
    }
    with open(RESULTS_FILE, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Wrote summary → {RESULTS_FILE}")

if __name__=="__main__":
    main()
