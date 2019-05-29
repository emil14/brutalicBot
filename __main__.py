import os
import asyncio

import aiohttp
from aiohttp import web


def main():
    async def client(base_url):
        async with aiohttp.ClientSession() as client:
            whconf = {'url': '...'}
            async with client.post(f'{base_url}/setWebhook', json=whconf) as r:
                print(await r.json())
            return client

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

    base_url = f'https://api.telegram.org/bot{os.environ["BOT_TOKEN"]}'
    loop = asyncio.get_event_loop()

    loop.run_until_complete(client(base_url))
    server(base_url)


if (__name__ == '__main__'):
    main()
