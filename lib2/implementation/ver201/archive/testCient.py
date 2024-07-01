import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = input("What's your message? ")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received from server: {response}")

asyncio.get_event_loop().run_until_complete(hello())