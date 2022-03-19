import api
from aiohttp import web
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

async def main():
    server = api.Client()
    await server.client.start(bot_token=server.bot_token)
    app = web.Application()
    app.add_routes(
        [
            web.get('/', server.hello),
            web.get('/favicon.ico', server.hello),
            web.get('/{id}', server.Downloader),
            web.get('/{id}/{name}', server.Downloader),
        ]
    )
    return app

if __name__ == "__main__":
    web.run_app(main(), port = 8000)