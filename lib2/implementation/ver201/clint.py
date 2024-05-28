import asyncio
import websockets

# Dictionary to keep track of connected clients
connected = set()
key = '0'

async def send_message():
    loop = asyncio.get_running_loop()
    while True:
        # Get user input asynchronously
        user_input = await loop.run_in_executor(None, input, "Enter a message to broadcast (press 'a' to broadcast a separate message): ")
        
        if user_input.lower() == 'a':
            # If 'a' is pressed, broadcast a separate message
            await asyncio.gather(*[client.send("Standard message for all clients") for client in connected])
        else:
            # Otherwise, broadcast the user's input message
            await asyncio.gather(*[client.send(user_input) for client in connected])

async def handle_client(websocket, path):
    # Add client to the set of connected clients
    connected.add(websocket)
    try:
        async for message in websocket:
            # When a message is received from a client
            print(f"Received message: {message}")
            
            # Broadcast the message to all connected clients
            # await asyncio.gather(*[client.send(message) for client in connected])
            await websocket.send(f" Hello {message}")
            print(f">>> {message}")

    finally:
        # Remove client from the set of connected clients when they disconnect
        connected.remove(websocket)

# Start the WebSocket server
start_server = websockets.serve(handle_client, "10.10.0.126", 8765)

# Start the coroutine to send messages
asyncio.ensure_future(send_message())

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()