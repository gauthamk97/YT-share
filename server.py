import asyncio
import websockets

USERS = set()

async def notify_all_users(message):
    await asyncio.wait([user.send(message) for user in USERS])

async def on_connection(websocket, path):
    USERS.add(websocket)
    try:
        async for message in websocket:
            print(f"< {message}")
            await notify_all_users(message)

    except:
        USERS.remove(websocket)
        print('connection closed for - ',websocket)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(on_connection, 'localhost', 12345))
asyncio.get_event_loop().run_forever()