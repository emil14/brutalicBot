import os
import asyncio

import aiohttp
from aiohttp import web

async def get_my_piblic_ip(client: aiohttp.ClientSession) -> dict:

    print(client.get('https://api.ipify.org/?format=json'))

async def set_webhooks(base_url):
    async with aiohttp.ClientSession() as client:
        my_public_ip = await get_my_piblic_ip(client) # fixme
        with open('./YOURPUBLIC.pem') as cert_file:
            async with client.post(f'{base_url}/setWebhook?url={my_public_ip}', data=cert_file) as resp:
                return await resp.json()

def server(base_url):
    async def handle_req(req):
        print(await req.json())
        return web.Response(status=200)

    async def index(req):
        print(await req.json())
        return web.Response(status=200, text='test text')

    app = web.Application()
    app.add_routes([
        web.post(f'/', index),
        web.post(f'/{base_url}/api/v1', handle_req)
    ])
    web.run_app(app)


def main():
    base_url = f'https://api.telegram.org/bot{os.environ["BOT_TOKEN"]}'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_webhooks(base_url))
    server(base_url)


if (__name__ == '__main__'):
    main()
