import asyncio
import websockets

USERS = set()

async def notify_all_users(message):
    await asyncio.wait([user.send(message) for user in USERS])

async def close_connection(user):
    USERS.remove(user)
    print('connection closed for - ',user)

async def on_connection(websocket, path):
    USERS.add(websocket)
    print('connection established for - ',websocket)
    try:
        async for message in websocket:
            print(f"< {message}")
            await notify_all_users(message)

    finally:
        await close_connection(websocket)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(on_connection, 'localhost', 12345))
asyncio.get_event_loop().run_forever()