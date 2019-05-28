import os
import asyncio

import aiohttp


def main():
    async def client(base_url):
        async with aiohttp.ClientSession() as session:
            whconf = {'url': '...'}
            await session.post(f'{base_url}/setWebhook', json=whconf)
            return session

    def server(base_url):
        async def handle_req(req):
            print(await req.json())
            return aiohttp.web.Response(status=200)

        app = aiohttp.web.Application()
        app.add_routes([aiohttp.web.post(f'/{base_url}/api/v1', handle_req)])
        aiohttp.web.run_app(app)

    base_url = f'https://api.telegram.org/bot{os.environ["BOT_TOKEN"]}'
    loop = asyncio.get_event_loop()

    loop.run_until_complete(client(base_url))
    server(base_url)


if (__name__ == '__main__'):
    main()
