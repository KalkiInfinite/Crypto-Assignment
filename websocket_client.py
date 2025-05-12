import asyncio
import websockets
import json

latest_orderbook = {"asks": [], "bids": []}

async def stream_data():
    uri = "wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/BTC-USDT-SWAP"
    async with websockets.connect(uri) as ws:
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            latest_orderbook["asks"] = data.get("asks", [])
            latest_orderbook["bids"] = data.get("bids", [])

def start_websocket():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(stream_data())
