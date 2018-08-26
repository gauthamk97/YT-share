import asyncio
import websockets
import copy

USERS = set()

async def notify_all_users_except_sender(message, sender):
    RECEIVERS = copy.copy(USERS)
    RECEIVERS.remove(sender)
    if RECEIVERS:
        await asyncio.wait([user.send(message) for user in RECEIVERS])
    del RECEIVERS

async def close_connection(user):
    USERS.remove(user)
    print('connection closed for - ',user)

async def on_connection(websocket, path):
    USERS.add(websocket)
    print('connection established for - ',websocket)
    try:
        async for message in websocket:
            print(f"< {message}")
            await notify_all_users_except_sender(message, websocket)

    except:
        print('Woah, something closed')
        
    finally:
        await close_connection(websocket)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(on_connection, 'localhost', 12345))
asyncio.get_event_loop().run_forever()